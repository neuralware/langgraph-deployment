from langchain_core.messages import HumanMessage
from langgraph.graph import END, START, StateGraph

from chat_agent.utils.nodes import chat
from chat_agent.utils.state import State

graph_builder = StateGraph(State)

graph_builder.add_node("chat", chat)

graph_builder.add_edge(START, "chat")
graph_builder.add_edge("chat", END)

graph = graph_builder.compile()
