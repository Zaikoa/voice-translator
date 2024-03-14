import language_tool_python

def grammar_check(text):
    tool = language_tool_python.LanguageTool('en-US')

    # Correct the errors
    corrected_text = tool.correct(text)
    
    print("Corrected test: %s\n", corrected_text)
    return corrected_text
