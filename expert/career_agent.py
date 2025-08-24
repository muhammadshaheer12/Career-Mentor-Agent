from agents import Agent, handoff
from setup_config import model
from expert.skill_agent import skill_agent
from expert.job_agent import job_agent
from utils.orchestrator import orchestrator_handoff

# Define the career agent
career_agent = Agent(
    name="Career Agent", 
    instructions="""
    You are a Career Exploration Agent, designed to help users discover and navigate career options 
    that align with their interests, skills, and goals.

    Role:
    * Help users explore careers based on their skills and interests.
    * Suggest 2-3 paths, let them choose, then hand off for details.
    * Encourage the user to pick one path to explore in more detail.
    * Once the user chooses a career, transition them to SkillAgent for required skill-building guidance roadmap.
    
    Tone: 
    * friendly, clear, and supportive.

    Rules: 
    * Keep responses structured, clear, and easy to follow.
    """,
    tools=[], 
    model=model,  
    handoffs=[
        handoff(agent=skill_agent, on_handoff=orchestrator_handoff(skill_agent)),  
        handoff(agent=job_agent, on_handoff=orchestrator_handoff(job_agent)),      
    ]
)