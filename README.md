# 💼 Career Mentor Agent  

An AI-powered **Career Mentor** built with **Chainlit**, **OpenAI Agents SDK**, and **Groq API**, designed to help users explore career opportunities, generate skill roadmaps, and receive personalized mentoring.  

---

## 🚀 Features  

- 💬 **Interactive Career Mentoring** — Understands your interests and guides you toward your dream career.  
- 🧠 **AI-Powered Roadmaps** — Uses `skill_roadmap_generator()` to create structured learning paths from beginner to expert.  
- 📈 **Advanced Career Roadmaps** — `get_career_roadmap()` for detailed progression planning.  
- 🔄 **Session-Based Conversations** — Keeps track of chat history for contextual replies.  
- ⚡ **Groq Integration** — Lightning-fast model inference with custom `RunConfig`.  

---

## 🛠 Tech Stack  

| Tool / Library         | Purpose |
|-----------------------|---------|
| ⚙️ **Chainlit**       | Chat interface |
| 🤖 **OpenAI Agents**  | AI agent execution |
| 🧩 **career_agent.py** | Career mentor logic |
| 🗂 **skill_roadmap_generator.py** | Generates skill development plans |
| 🚀 **Groq API**       | Model provider |
| 🐍 **Python**         | Core programming language |

---

## 📂 Project Structure  

```
📦 project/
 ┣ 📂 expert/
 ┃ ┣ 📜 career_agent.py        # AI career mentor logic
 ┃ ┣ 📜 job_agent.py           # Job-related agent logic
 ┃ ┗ 📜 skill_agent.py         # Skill guidance agent logic
 ┣ 📂 tools/
 ┃ ┗ 📜 skill_roadmap_generator.py # Generates skill roadmaps
 ┣ 📂 utils/
 ┃ ┗ 📜 orchestrator.py        # Orchestrates multi-agent flow
 ┣ 📜 setup_config.py          # Model & API configuration
 ┣ 📜 .env                     # Environment variables
 ┣ 📜 main.py                  # Main Chainlit app entry point
 ┗ 📜 README.md                # Project documentation
```

---

## ⚡ Quick Start  

1️⃣ **Clone the repository**  
```bash
git clone https://github.com/muhammadshaheer12/Career-Mentor-Agent
cd Career-Mentor-Agent
```

2️⃣ **Create and activate a uv virtual environment**
```bash
uv venv
```
**Activate venv:**  
- **Windows (PowerShell)**  
  ```powershell
  .venv\Scripts\activate
  ```
- **macOS/Linux**  
  ```bash
  source .venv/bin/activate
  ```
  
3️⃣ **Set up environment variables in .env**
```
GROQ_API_KEY=your_groq_api_key
```

4️⃣ **Run the app**  
```bash
chainlit run main.py 
```

---
