import speech_recognition as sr

# inits the model for the language that we will be using
model = Model(r"models/vosk-model-small-en-us-0.15/vosk-model-small-en-us-0.15")

# Setting the rate inside the recognizer
recognizer = KaldiRecognizer(model, 44100)

with sr.Microphone() as source:
    # read the audio data from the default microphone
    audio_data = recognizer.record(source, duration=5)
    print("Recognizing...")
    # convert speech to text
    text = recognizer.recognize_google(audio_data)
    print(text)