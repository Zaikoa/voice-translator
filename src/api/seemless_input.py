import time
import speech_recognition as sr
from transformers import AutoProcessor, SeamlessM4TModel

# Load the processor and model
processor = AutoProcessor.from_pretrained("facebook/hf-seamless-m4t-medium")
model = SeamlessM4TModel.from_pretrained("facebook/hf-seamless-m4t-medium")

def recognize_speech():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Raedy")
        audio = recognizer.listen(source, timeout=5)

    try:

        # straight from the seamless mode
        text_inputs = processor(audios=audio, sampling_rate=16000, return_tensors="pt")
        output_tokens = model.generate(**text_inputs, tgt_lang="eng", generate_speech=False)
        translated_text = processor.decode(output_tokens[0].tolist()[0], skip_special_tokens=True)

        # Should print the text out but it doesnt
        print("Translation:", translated_text)
    except sr.UnknownValueError:
        print("Could not understand audio")
    except sr.RequestError as e:
        print(f"Error connecting to the speech service: {e}")

while True:
    recognize_speech()
    print("Waiting")
    time.sleep(5)
