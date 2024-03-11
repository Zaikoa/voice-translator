import keyboard
from vosk import Model, KaldiRecognizer
import pyaudio

# inits the model for the language that we will be using
model = Model(r"models/vosk-model-small-en-us-0.15/vosk-model-small-en-us-0.15")

# Setting the rate inside the recognizer
recognizer = KaldiRecognizer(model, 44100)

# initilizing the port audio 
mic = pyaudio.PyAudio()

# Starts recording voice 
stream = mic.open(format=pyaudio.paInt16, channels=1, rate=44100, input=True, frames_per_buffer=8192)
stream.start_stream()

# Loops through and prints out what is said, if control-C is pressed, exit

def run_input_acceptor():
    while True:
        data = stream.read(4096)

        # Exits when given the exit keys
        if(keyboard.is_pressed("ctrl+c")):
            print("Breaking out volentarily")
            break

        if recognizer.AcceptWaveform(data):
            text = recognizer.Result()
            #print(text[14:-3])
            return text[14:-3]