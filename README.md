# CLI Task Manager

A command-line task manager with built-in AI assistance built with Python.

## Features
- Add, view, complete, and delete tasks
- AI-powered priority and time estimation using Groq LLaMA
- Color-coded priority display in terminal
- Persistent JSON storage
- Filter tasks by status or priority

## Tech Stack
- Python 3.11
- Groq API (LLaMA 4 Scout)
- python-dotenv

## Project Structure
task-manager/

├── main.py         # CLI interface and entry point

├── manager.py      # Core logic and operations

├── task.py         # Task class definition

├── storage.py      # JSON file persistence

├── ai_helper.py    # Groq AI integration

├── decorators.py   # Custom logging decorator

├── data/

│   └── tasks.json  # Persistent storage

└── .env            # API keys (never committed)

## Setup
1. Clone the repo
2. Create a virtual environment: `python -m venv venv`
3. Activate it: `venv\Scripts\activate`
4. Install dependencies: `pip install groq python-dotenv`
5. Create `.env` file and add your Groq key: `GROQ_API_KEY=your_key`
6. Run: `python main.py`