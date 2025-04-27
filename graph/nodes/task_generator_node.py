# graph/nodes/task_generator_node.py
from langchain_core.messages import HumanMessage, AIMessage
from agents.task_geenerator import task_generator

def task_generator_node(state):
    # Get last message content
    last_message = state["messages"][-1].content  # Access content property
    
    # Generate tasks
    response = task_generator(last_message)
    # print(f"Response: {response}")
    # Update state
    if hasattr(response, "input_required"):
        state["input_required"] = response.input_required
    
    
    # Add tasks to state
    state["messages"].append(
        AIMessage(content=f"Tasks generated successfully: {response.tasks}")
    )
    state["tasks"] = response.tasks
    state["status"] = "complete"
    # print(f"Tasks: {state['tasks']}")
    # state["tasks"].extend([task.dict() for task in response.tasks])
    
    return state
