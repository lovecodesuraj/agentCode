
from langgraph.checkpoint.memory import MemorySaver
from langgraph.graph import StateGraph, START, END
from typing import Literal
from graph.state import State
from graph.nodes import human_feedback_node, validator_node, task_generator_node, code_generator_node


graph_builder = StateGraph(State)

graph_builder.add_node("human_feedback_node", human_feedback_node)
graph_builder.add_node("validator_node", validator_node)
graph_builder.add_node("task_generator_node", task_generator_node)
graph_builder.add_node("code_generator_node", code_generator_node)



# Edge Definitions
graph_builder.add_edge(START, "validator_node")
graph_builder.add_edge("human_feedback_node", "validator_node")

def validator_edge_selector(state: State) -> Literal["human_feedback_node", "task_generator_node"]:
    return "human_feedback_node" if state["input_required"] else "task_generator_node"

graph_builder.add_conditional_edges(
    "validator_node",
    validator_edge_selector,
    {"human_feedback_node": "human_feedback_node", "task_generator_node": "task_generator_node"}
)

graph_builder.add_edge("task_generator_node", "code_generator_node")
graph_builder.add_edge("code_generator_node", END)


graph = graph_builder.compile(checkpointer=MemorySaver())
