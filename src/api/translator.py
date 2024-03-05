from translate import Translator

# Inits translater to designated language
translator= Translator(to_lang="ja")

# When passing in a string, returns translated text
def translate(argument):
    translation = translator.translate(argument)
    return translation