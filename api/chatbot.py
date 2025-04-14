import os

from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from dotenv import load_dotenv
from pydantic import BaseModel

load_dotenv(dotenv_path=".env.local")

openai_api_key = os.getenv("OPENAI_API_KEY")

non_streaming_model_openai = ChatOpenAI(
    api_key=openai_api_key, model="gpt-4o", temperature=0, streaming=False
)

process_customer_query_prompt = """You are an expert Customer Support Service Staff. You can understand and respond to customer 
queries related to booking, cancellation, and pricing. You can also take action on behalf of the client according to the requests, 
for example, reschedule booking at a given date and time. Your responses must be helpful, concise, and proactive."""

class CustomerQueryResponse(BaseModel):
    intent: str
    response: str

def process_customer_query(customer_query: str):
    prompt = ChatPromptTemplate.from_messages(
        [("system", process_customer_query_prompt), ("user", "{customer_query}")]
    )

    runnable = prompt | non_streaming_model_openai.with_structured_output(
        schema=CustomerQueryResponse
    )

    return runnable.invoke({"customer_query": customer_query}).model_dump()