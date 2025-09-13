# voice-assistant-elevenlabs
A voice-based virtual assistant built using the ElevenLabs API.  
This project allows users to interact with a virtual assistant that can understand schedules, respond via voice, and handle interruptions or corrections.

> ⚠️ **Note:** This project was implemented following a tutorial by another author, with some modifications and personalization.

---

## Features

- Responds to user queries via voice.
- Reads and interprets user schedules.
- Handles interruptions and corrections in real-time.
- Customizable prompts and first messages.
- Uses ElevenLabs TTS and conversational AI capabilities.

---

## Installation

1. **Clone the repository:**
```bash
git clone <your-repo-url>
cd internshipprojects2026

2.Install dependencies:
pip install -r requirements.txt

3.Set up environment variables:
Create a .env file in the project root and add your ElevenLabs credentials:
AGENT_ID=<your_agent_id>
API_KEY=<your_api_key>

4.Usage
Run the voice assistant:
python fridayVA.py

5.Dependencies
Python 3.11+
elevenlabs 1.54.0 
python-dotenv 1.0.1
pyaudio
