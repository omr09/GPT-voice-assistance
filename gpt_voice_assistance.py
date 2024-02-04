import openai
import elevenlabs
import speech_recognition as sr
from queue import Queue

# API
openai.api_key = "YOUR-API-KEY-GOES-HERE"
elevenlabs.set_api_key("YOUR-API-KEY-GOES-HERE") 

# voice
bella_voice_identifier = "EXAVITQu4vr4xnSDxMaL"

transcript_queue = Queue()

def on_data(audio_data):
    recognizer = sr.Recognizer()
    try:
        transcript = recognizer.recognize_google(audio_data)
        if transcript:
            transcript_queue.put(transcript)
            print("User:", transcript, end="\r\n")
    except sr.UnknownValueError:
        pass  

def on_error(error):
    print("An error occurred:", error)

# Conversation loop
def handle_conversation():
    while True:
        recognizer = sr.Recognizer()

        
        with sr.Microphone(sample_rate=44100) as source:
            print("Listening...")
            audio_data = recognizer.listen(source, timeout=None, phrase_time_limit=10)

        # Process the audio data
        on_data(audio_data)

        
        transcript_result = transcript_queue.get()

        
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": 'You are a highly skilled AI, answer the questions given within a maximum of 100 characters.'},
                {"role": "user", "content": transcript_result}
            ]
        )

        text = response['choices'][0]['message']['content']

        
        audio = elevenlabs.generate(
            text=text,
            voice=bella_voice_identifier
        )

        print("\nAI:", text, end="\r\n")

        
        elevenlabs.play(audio)

handle_conversation()
