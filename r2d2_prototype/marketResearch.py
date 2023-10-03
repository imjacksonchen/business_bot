import os

from langchain.llms import OpenAI
from langchain.agents import AgentType, initialize_agent, load_tools
from langchain.utilities import SerpAPIWrapper

# Use LangChain to get latest competitor information/research

def gather_intelligence(company):
    os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
    os.environ["SERPAPI_API_KEY"] = os.getenv("SERPAPI_API_KEY")

    llm = OpenAI(temperature=0)
    tools = load_tools(["serpapi"], llm=llm)
    agent = initialize_agent(tools, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose = False)

    prompt = "What is the latest news from {}?".format(company)

    return agent.run(prompt)


print(gather_intelligence("Tesla"))