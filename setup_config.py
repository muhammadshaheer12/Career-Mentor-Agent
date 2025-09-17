import os
from dotenv import load_dotenv 
from agents import AsyncOpenAI, OpenAIChatCompletionsModel, RunConfig

# Load environment variables
load_dotenv()

# Get Groq API key from environment
api_key = os.getenv("GROQ_API_KEY")
if not api_key:
    raise ValueError("GROQ_API_KEY not set in .env file")

#Set up AsyncOpenAI external client with Groq base URL
external_client = AsyncOpenAI(
    api_key=api_key,
    base_url="https://api.groq.com/openai/v1"
)

# Initialize the OpenAIChatCompletionsModel with the configure external client
model = OpenAIChatCompletionsModel(
    openai_client=external_client,
    model="llama-3.3-70b-versatile"
)

# Configuration for running Groq model without tracing
groq_config = RunConfig(
    model=model,
    model_provider=external_client,
    tracing_disabled=True
)
