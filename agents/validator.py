import os
from dotenv import load_dotenv
load_dotenv()

from langchain_core.pydantic_v1 import BaseModel, Field
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import ChatPromptTemplate
from llms.llms import gemini_llm, groq_llm 
from models.response import QueryValidatorResponse


# Wrap with structured output
# structured_llm = gemini_llm.with_structured_output(QueryValidatorResponse)
structured_llm = groq_llm.with_structured_output(QueryValidatorResponse)

# Now define a strong system prompt
system_prompt = """
You are an expert software architect assistant.

Your job is to:
1. Analyze the user's request for building a project or system.
2. Check if enough information is available to start designing the solution.
3. If any important information is missing, clearly list what information is needed.

Respond using these rules:
- If everything needed is already present, set `input_required` to false, and leave `missing_info` empty.
- If anything is missing, set `input_required` to true, and clearly mention what extra information is needed in `missing_info`.

Be professional but friendly.
"""

# Create a full prompt template
prompt = ChatPromptTemplate.from_messages([
    ("system", system_prompt),
    ("human", "{input}")
])

# Bind the prompt
chain = prompt | structured_llm

# Test
# user_input = "Build an agentic HR system for resume matching"



# Output
# print(f"\nAgent Response: {response.response}")
# print(f"Is more info required?: {response.input_required}")
# print(f"Missing Info: {response.missing_info}")

def validator(conversation):
   response = chain.invoke({"input": conversation})
   return response