# Voice-Based AI Chatbot with OpenAI and ElevenLabs

## Overview

This project demonstrates a voice-based AI chatbot that utilizes OpenAI's GPT-3.5 Turbo for natural language processing and ElevenLabs for text-to-speech synthesis. The chatbot listens to user input through the microphone, sends the transcript to OpenAI for response generation, and plays the AI response using ElevenLabs.

## Requirements

- Python 3.11
- OpenAI API key
- ElevenLabs API key
- SpeechRecognition library
- OpenAI Python library
- ElevenLabs Python library
- FFmpeg (for audio playback)

## Setup

1. **Install Python dependencies:**

   ```bash
   pip install openai elevenlabs SpeechRecognition
Install FFmpeg for audio playback. You can download it from https://ffmpeg.org/download.html.

Set your API keys:

OpenAI: Replace "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" with your OpenAI API key.
ElevenLabs: Replace "b84e2980716d597b37c85012db8cb7d5" with your ElevenLabs API key.
Run the script:

bash
python hi.py
Usage
The chatbot will continuously listen for user input.
Speak clearly into the microphone and wait for the AI response.
The AI response will be played using ElevenLabs.
Notes
If you encounter issues with audio playback, ensure that FFmpeg is installed and in your system's PATH. Alternatively, provide the path to the ffplay executable in the script.
References
OpenAI: https://beta.openai.com/
ElevenLabs: https://eleven-labs.com/
