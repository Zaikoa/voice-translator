import numpy as np
import pyaudio
from transformers import AutoProcessor, SeamlessM4TModel

# Load the processor and model
processor = AutoProcessor.from_pretrained("facebook/hf-seamless-m4t-medium")
model = SeamlessM4TModel.from_pretrained("facebook/hf-seamless-m4t-medium")

# All calculated using google
FORMAT = pyaudio.paInt16
CHANNELS = 1 
RATE = 16000
CHUNK = 3200

# might stop the processor from spewing out random words
SPEECH_THRESHOLD = 1500

mic = pyaudio.PyAudio()

# Starts recording
stream = mic.open(format=FORMAT, channels=CHANNELS, rate=RATE, input=True, frames_per_buffer=CHUNK)
stream.start_stream()

def start_listening():
    print("Listening")
    
    # Capture audio from the microphone
    audio_frames = []
    for _ in range(int(RATE / CHUNK * 5)):
        data = stream.read(CHUNK)
        audio_frames.append(np.frombuffer(data, dtype=np.int16))
    
    # Convert the list of audio frames to a NumPy array (seamless needs it)
    audio_data = np.concatenate(audio_frames, axis=0)

    # If above threshold (Trying to get rid of random translation and such)
    if np.max(np.abs(audio_data)) > SPEECH_THRESHOLD:

        # Convert the audio data
        text_inputs = processor(audios=np.expand_dims(audio_data, axis=0), sampling_rate=RATE, return_tensors="pt")

        # Transform the input into text and then print it
        output_tokens = model.generate(**text_inputs, tgt_lang="eng", generate_speech=False)
        translated_text = processor.decode(output_tokens[0].tolist()[0], skip_special_tokens=True)
        print("English: %s\n", translated_text)
        return translated_text