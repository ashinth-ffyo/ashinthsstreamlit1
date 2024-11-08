import pyttsx3

# Initialize the TTS engine
engine = pyttsx3.init("sapi5")

# List available voices
voices = engine.getProperty('voices')

# Adjust properties for a friendlier tone
engine.setProperty('rate', 170)    # Adjust speed of speech
engine.setProperty('volume', 1)  # Volume (0.0 to 1.0)

# Function to make the program talk
def speak(text):
    engine.say(text)
    engine.runAndWait()

