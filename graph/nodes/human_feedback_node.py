from langchain_core.messages import HumanMessage

def human_feedback_node(state):
    last_content = state["messages"][-1].content if state["messages"] else ""
    
    feedback = input(f"Feedback required for: {last_content}\n> ")
    state["messages"].append(HumanMessage(content=feedback))
    state["input_required"] = False
    return state
    
    
    
   
