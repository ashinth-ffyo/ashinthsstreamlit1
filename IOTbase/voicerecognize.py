import speech_recognition as sr
from IOTbase import speech as sp

stat = ""
s = ""

recognizer = sr.Recognizer()

def capture_voice_input():
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
    return audio

def convert_voice_to_text(audio):
    try:
        text = recognizer.recognize_google(audio)
        print("You said: " + text)
    except sr.UnknownValueError:
        text = ""
        print("Sorry, I didn't understand that.")
    except sr.RequestError as e:
        text = ""
        print("Error; {0}".format(e))
    return text

def process_voice_command(text):
    global s
    if "hello" in text.lower():
        sp.speak("Hello! How can I help you?")

    elif "switch on light" in text.lower():
        sp.speak("switching on lights")
        s = "on"

    elif "switch off light" in text.lower():
        sp.speak("Switching off lights")
        s = "off"
     
    elif "light status" in text.lower():
        stat = ("Light is", s)
        sp.speak(stat)

    elif "goodbye" in text.lower():
        sp.speak("Goodbye! Have a great day!")
        return True
    else:
        sp.speak("I didn't understand that command. Please try again.")
    return False
