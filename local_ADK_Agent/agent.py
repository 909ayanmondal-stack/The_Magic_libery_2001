from google.adk.agents.llm_agent import Agent
from google.adk.models import LiteLlm



root_agent = Agent(
    model=LiteLlm(
        model='ollama/llama3.1:latest',
    ),
    name='root_agent',
    description='A helpful assistant for user questions.',
    instruction="""You are a helpful assistant
    your task is to recommend food based on the city name
    if the city name is not provided then ask the user for the city name
    """,
)







