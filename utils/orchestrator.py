from agents import Agent, RunContextWrapper
import chainlit as cl

# Handoff control to another agent
def orchestrator_handoff(agent: Agent):
    async def _on_handoff(ctx: RunContextWrapper[None]):
        await cl.Message(
            content=f"Handing off to *{agent.name}*..."
        ).send()
        cl.user_session.set("agent", agent) 
    return _on_handoff
