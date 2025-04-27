
import os
from dotenv import load_dotenv
load_dotenv()




#gemini-llm
from langchain_google_genai import ChatGoogleGenerativeAI

GOOGLE_API_KEY=os.getenv("GOOGLE_API_KEY")
GEMINI_MODEL=os.getenv("GEMINI_MODEL")

print(f"GOOGLE_API_KEY: {GOOGLE_API_KEY}")
print(f"GEMINI_MODEL: {GEMINI_MODEL}")

gemini_llm = ChatGoogleGenerativeAI(
    model=GEMINI_MODEL,
    google_api_key=GOOGLE_API_KEY
)





#groq
from langchain_groq import ChatGroq

GROQ_API_KEY=os.getenv("GROQ_API_KEY")
GROQ_MODEL=os.getenv("GROQ_MODEL")

print(f"GROQ_API_KEY: {GROQ_API_KEY}")
print(f"GROQ_MODEL: {GROQ_MODEL}")

groq_llm = ChatGroq(
    model=GROQ_MODEL,
    api_key=GROQ_API_KEY
)




