from dotenv import load_dotenv
import os

from langchain.llms import OpenAI
from langchain.agents import AgentType, initialize_agent, load_tools

# Use LangChain to get latest competitor information/research

def gather_intelligence(company):
    load_dotenv("keys.env")
    os.environ["OPENAI_API_KEY"] = os.getenv("OPEN_AI_API_KEY")
    os.environ["SERPAPI_API_KEY"] = os.getenv("SERPAPI_API_KEY")

    llm = OpenAI(temperature=0)
    tools = load_tools(["serpapi", "wikipedia"], llm=llm)
    agent = initialize_agent(tools, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose = False)

    prompt = "What is the latest product from {}? What is the current sentiment of it? What is the latest news on them?".format(company)

    return agent.run(prompt)