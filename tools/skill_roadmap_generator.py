import os
from dotenv import load_dotenv
from agents import function_tool, AsyncOpenAI, RunContextWrapper

# Load environment variables
load_dotenv()

# Get API key from .env
api_key = os.getenv("GROQ_API_KEY")

# Initialize the client
client = AsyncOpenAI(
    api_key=api_key,
    base_url=" https://api.groq.com/openai/v1"
)

@function_tool
async def get_career_roadmap(wrapper: RunContextWrapper):
    try:
        prompt = (
            f"You are a career mentor. The user wants to become a {input['career_field']}.\n"
            "Create a step-by-step learning plan from beginner to advanced level.\n"
            "Include technical skills, soft skills, and practical projects.\n"
            "Format the response in clear numbered steps."
        )

        # Call the model
        response = await client.chat.completions.create(
            model="llama3-70b-8192",
            messages=[{"role": "user", "content": prompt}]
        )

        # Extract output
        output = response.choices[0].message.content

        return {
            "skill_roadmap": output.strip()
        }

    except Exception as e:
        print("Exception in skill_roadmap_generator:", str(e))
        return {
            "error": f"Exception in skill_roadmap_generator: {str(e)}"
        }