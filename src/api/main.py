from vosk_input import *
from translator import *
from text_to_speech import *
import sys
import io



if __name__ == "__main__":

    # Handles printing Japanese characters to terminal
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
    while True:
        sentence = run_input_acceptor()
        translated_value = translate(sentence)

        print(translated_value)

        speak_language(translated_value)
        if(keyboard.is_pressed("ctrl+c")):
            print("Breaking out volentarily")
            break
