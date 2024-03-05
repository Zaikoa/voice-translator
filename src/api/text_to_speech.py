import pyttsx3


engine = pyttsx3.init()
voices = engine.getProperty('voices')

# Japanese voice audio
engine.setProperty("voice", voices[2].id)

# Slowing down the speech
rate = engine.getProperty('rate')
engine.setProperty('rate', rate-50)

def speak_language(sentence):
    engine.say(sentence)
    engine.runAndWait()