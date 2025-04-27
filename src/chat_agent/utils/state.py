from operator import add
from typing import Annotated, TypedDict
from langchain_core.messages import AnyMessage


class State(TypedDict):
    messages: Annotated[list[AnyMessage], add]  # Accumulates messages
