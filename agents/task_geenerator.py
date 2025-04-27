import os
from dotenv import load_dotenv
load_dotenv()

from langchain.prompts import ChatPromptTemplate
from models.response import TaskGeneratorResponse
from llms.llms import gemini_llm as model, groq_llm 

# structured_llm=model.with_structured_output(TaskGeneratorResponse)
structured_llm=groq_llm.with_structured_output(TaskGeneratorResponse)

# Now define a strong system prompt
system_prompt = """
You are an expert software project planner and architect.

Your job is to:
- Read the user's clarified project description carefully.
- Break down the high-level project into clear, manageable subtasks.
- For each subtask, define:
  - A unique ID (like "task-1", "task-2", etc.)
  - A short description of the task
  - A list of dependencies (task IDs it depends on)

Your response must follow these rules:
- If you need more information from the user to complete the breakdown, set `is_finalized` to false and clearly mention what information is missing.
- If you have everything needed, set `is_finalized` to true and leave `missing_info` empty.
- Your response must strictly match the structure of the following Python Pydantic model:

Be concise, clear, and professional.
Always respect task dependencies if one task must be completed before another.

Start when ready.

"""

# Create a full prompt template
prompt = ChatPromptTemplate.from_messages([
    ("system", system_prompt),
    ("human", "{input}")
])

# Bind the prompt
chain = prompt | structured_llm

def task_generator(summary):
   response = chain.invoke({"input": summary})
   return response