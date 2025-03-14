import speech_recognition as sr
import pyttsx3
import google.generativeai as genai
import webbrowser
import datetime

# API Key for Google Generative AI
apikey = "AIzathBpgnQld7P3tXaACv7Zaz5MNk188dvrlOxIQ"

# Configure Google Generative AI
genai.configure(api_key=apikey)

# Initialize chat session variable
chat_session = None

def chat(query):
global chat_session
try:
# If no chat session exists, start a new one
if chat_session is None:
chat_session = genai.GenerativeModel(model_name="gemini-1.5-flash").start_chat()

# Send the query to the model
response = chat_session.send_message(query)

# Get model response
model_response = response.text
print(f"Jarvis: {model_response}")
say(model_response)
except Exception as e:
print(f"Request failed: {e}")
say("Error generating response.")

def say(text):
# Use pyttsx3 for text-to-speech
engine = pyttsx3.init()
engine.say(text)
engine.runAndWait()

def takeCommand():
r = sr.Recognizer()
with sr.Microphone() as source:
print("Listening...")
audio = r.listen(source)
try:
print("Recognizing...")
query = r.recognize_google(audio, language="en-in")
print(f"User said: {query}")
return query
except Exception as e:
print("Sorry, I didn't catch that.")
return "Error"


if __name__ == '__main__':
print('Welcome')
say("Welcome sir")

while True:
query = takeCommand().lower()

# Example commands to open sites
if "open youtube" in query:
say("Opening YouTube, sir...")
webbrowser.open("https://www.youtube.com")
elif "open google" in query:
say("Opening Google, sir...")
webbrowser.open("https://www.google.com")
elif "the time" in query:
current_time = datetime.datetime.now().strftime("%H:%M")
say(f"The time is {current_time}")
elif "exit" in query or "quit" in query:
say("Goodbye, sir!")
break
elif "reset chat" in query:
chat_session = None
say("Chat history reset.")
else:
chat(query)

