import uuid
from langchain_core.messages import HumanMessage, AIMessage
from graph.graph import graph

class TerminalOrchestrator:
    def __init__(self):
        self.thread_id = str(uuid.uuid4())
        self.state = {
            "messages": [],
            "status": "waiting_input",
            "input_required": False,
            "tasks": [],
            "code": ""
        }
        self.started = False

    def display_state(self):
        print("\n=== Current State ===")
        print(f"Thread ID: {self.thread_id}")
        print(f"Status: {self.state['status']}")
        print(f"Tasks: {len(self.state['tasks'])}")
        print(f"Code: {self.state['code']}")
        print("Messages:")
        for msg in self.state["messages"]:
            if isinstance(msg, HumanMessage):
                print(f"  User: {msg.content}")
            else:
                print(f"  Assistant: {msg.content}")
        print("====================\n")

    def run(self):
        print("Workflow Orchestrator Initialized")
        
        # Initial input
        if not self.started:
            user_input = input("Enter your project requirements: ")
            self.state["messages"].append(HumanMessage(content=user_input))
            self.state["status"] = "processing"
            self.started = True

        # Main loop
        while self.state["status"] != "complete":
            # Display current state
            self.display_state()

            # Execute graph (input handled within nodes)
            try:
                print("Processing workflow...")
                result = graph.invoke(
                    self.state,
                    config={"configurable": {"thread_id": self.thread_id}}
                )
                self.state.update(result)
            except Exception as e:
                print(f"Error: {str(e)}")
                self.state["status"] = "failed"
                break

        # Final output
        print("\nFinal State:")
        self.display_state()
        if self.state["status"] == "complete":
            print("Workflow Completed Successfully!")
        else:
            print("Workflow Failed!")

if __name__ == "__main__":
    orchestrator = TerminalOrchestrator()
    orchestrator.run()
