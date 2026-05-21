#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from langchain.agents import initialize_agent
from langchain.chat_models import ChatOpenAI

from tools import (
    flight_tool,
    hotel_tool,
    places_tool
)

llm = ChatOpenAI(
    temperature=0
)

tools = [
    flight_tool,
    hotel_tool,
    places_tool
]

agent = initialize_agent(
    tools,
    llm,
    agent="zero-shot-react-description",
    verbose=True
)

response = agent.run(
    "Find flights from Delhi to Goa"
)

print(response)


# In[ ]:




