from agents.code_generator import code_generator
from langchain_core.messages import AIMessage
import os
import uuid
def code_generator_node(state):
    last_message = state["messages"][-1].content

    response = code_generator(last_message, state["tasks"])
    os.makedirs("code", exist_ok=True)
    for file in response.files:
        with open(f"code/{file.name}", "w") as f:
            f.write(file.content)
    state["messages"].append(AIMessage(content=response.message))
    state["status"] = "complete"
    return state

