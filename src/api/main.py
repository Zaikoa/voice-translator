from translator import *
from text_to_speech import *
from grammar import *
from seemless import *
import sys
import io



if __name__ == "__main__":

    # Handles printing Japanese characters to terminal
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
    while True:
        sentence = start_listening()
        corrected = grammar_check(sentence)
        translated_value = translate(corrected)
        print(translated_value)

        speak_language(translated_value)
