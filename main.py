import chainlit as cl
from agents.run import RunConfig
from agents import Runner
from expert.career_agent import career_agent
from setup_config import groq_config

# Sends a welcome message to the user
@cl.on_chat_start
async def on_chat_start():
    cl.user_session.set("chat_history", [])
    await cl.Message("Welcome! I'm your Career Mentor.Share your skills, interests, or dream career, and I'll guide you!").send()

# Handle incoming messages in Chainlit
@cl.on_message
async def handle_message(message: cl.Message):
    try:
        chat_history = cl.user_session.get("chat_history", [])
        chat_history.append({"role": "user", "content": message.content})

        result = await Runner.run(
            career_agent,
            input=chat_history,
            run_config=groq_config
        )

        await cl.Message(content=result.final_output).send()

        chat_history = result.to_input_list()
        cl.user_session.set("chat_history", chat_history)
        
    except Exception as e:
        await cl.Message(content=f"Error: {e}").send()