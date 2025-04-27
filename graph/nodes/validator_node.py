from agents.validator import validator
from langchain_core.messages import HumanMessage, AIMessage

def validator_node(state):
    # Convert message objects to conversation string
    conversation = "\n".join(
        f"{msg.type}: {msg.content}"  # Use .type instead of .role
        for msg in state["messages"]
    )

    # Get validation response
    response = validator(conversation)
    
    # Update state with proper message objects
    state["input_required"] = response.input_required
    
    if response.input_required:
        # Add missing info request as AI message
        state["messages"].append(
            AIMessage(content=f"Additional information needed: {response.missing_info}")
        )
    else:
        # Add validation result as AI message
        state["messages"].append(
            AIMessage(content=response.response)
        )
        # state["input_required"] = False
    
    return state
