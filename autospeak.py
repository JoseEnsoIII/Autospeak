import pyttsx3

# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Set the speed of speech (words per minute)
engine.setProperty('rate', 150)

# Set the voice type
voices = engine.getProperty('voices')
engine.setProperty('voice', 'ravenna') # Change the index to select a different voice

# Enter the text to be spoken
text = input("Enter the text you want to be spoken: ")

# Auto-speak the text
engine.say(text)
engine.runAndWait()
