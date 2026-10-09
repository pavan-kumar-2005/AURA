AURA — Artificial Unified Responsive Assistant

AURA is a Python-based personal AI assistant designed to interact with users through voice commands, answer questions using a locally running Large Language Model (LLM), and perform useful everyday tasks.

Features

- Voice Interaction: Listen to user commands and respond using speech.
- Local AI Integration: Uses Ollama with the Llama 3.2 (3B) model to generate AI responses locally.
- Conversational Memory: Stores conversation history to support more personalized interactions.
- Weather Updates: Retrieves weather information using the OpenWeatherMap API.
- Time and Date: Provides current time and date information.
- System Controls: Supports selected system operations through commands.
- Productivity Features: Includes modules for notes, music, news, and other assistant functions.
- Modular Architecture: Organizes features into separate Python modules for easier maintenance.

Technologies Used

- Language: Python
- AI Runtime: Ollama
- Language Model: Llama 3.2 (3B)
- Speech: pyttsx3 and the project's listening module
- Environment Variables: python-dotenv
- External API: OpenWeatherMap
- Version Control: Git and GitHub

Project Structure

AURA/
├── main.py
├── file_handling.py
├── requirements.txt
├── modules/
│   ├── ai_brain.py
│   ├── commands.py
│   ├── information.py
│   ├── listen.py
│   ├── memory.py
│   ├── mouse_control.py
│   ├── music.py
│   ├── news.py
│   ├── notes.py
│   ├── password.py
│   ├── screenshot.py
│   ├── speak.py
│   ├── system_control.py
│   ├── system_info.py
│   └── weather.py
├── memory/
├── logs/
├── screenshots/
└── .env

Prerequisites

- Python installed on your computer
- Ollama installed and running
- The Llama 3.2 (3B) model downloaded through Ollama
- Required Python packages
- An OpenWeatherMap API key for weather functionality

Installation and Setup

1. Clone the repository

git clone https://github.com/pavan-kumar-2005/AURA.git
cd AURA

2. Create and activate a virtual environment

Windows PowerShell:

python -m venv .venv
.\.venv\Scripts\Activate.ps1

3. Install dependencies

pip install -r requirements.txt

4. Set up Ollama

Install Ollama from https://ollama.com/ and download the model:

ollama pull llama3.2:3b

5. Configure environment variables

Create a ".env" file in the project root:

WEATHER_API_KEY=your_openweathermap_api_key

Keep API keys private. Never upload your ".env" file to GitHub.

6. Run AURA

python main.py

How It Works

1. AURA initializes its core modules.
2. It listens for a user's voice command.
3. The command processor handles supported tasks or forwards general questions to the local LLM.
4. The AI module generates a response using Ollama.
5. The assistant speaks the response and uses conversational memory where implemented.

Future Improvements

- Improve speech recognition accuracy.
- Enhance conversational memory management.
- Add more voice-controlled operations.
- Improve response speed and error handling.
- Expand the assistant's capabilities.

Author

Pavan Kumar

GitHub: https://github.com/pavan-kumar-2005

---

AURA is an ongoing personal project focused on exploring Python, local AI, voice interaction, and intelligent automation.