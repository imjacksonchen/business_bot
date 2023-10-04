import os

from langchain.llms import OpenAI
from langchain.agents import AgentType, initialize_agent, load_tools

# Use LangChain to get latest competitor information/research

def gather_intelligence(company):

    # API keys
    os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
    os.environ["SERPAPI_API_KEY"] = os.getenv("SERPAPI_API_KEY")

    # Configure the agent and tools to allow langchain to run
    llm = OpenAI(temperature=0)
    tools = load_tools(["serpapi, wikipeida"], llm=llm)
    agent = initialize_agent(tools, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose = False)

    # Prompt to get latest news on a compnay and their product
    prompt = "What is the latest product from {}? What is the current sentiment of it? What is the latest news on them?".format(company)

    return agent.run(prompt)