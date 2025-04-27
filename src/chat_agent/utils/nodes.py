from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
from langchain_core.messages import SystemMessage

from chat_agent.utils.state import State

_ = load_dotenv()

model = init_chat_model(model="gpt-4o", model_provider="openai")

instructions = (
    "You are a Marketing Research Assistant. "
    "Your task is to analyze market trends, competitor strategies, "
    "and customer insights. "
    "Provide concise, data-backed summaries and actionable recommendations. "
)
system_message = [SystemMessage(content=instructions)]


def chat(state: State) -> dict:
    messages = system_message + state["messages"]
    message = model.invoke(messages)  # Generate response
    return {"messages": [message]}  # Return updated messages
