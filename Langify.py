import langid
from langdetect import detect, DetectorFactory
from langdetect.lang_detect_exception import LangDetectException
from colorama import init, Fore, Style
import langcodes
import sys
import time

init(autoreset=True)
DetectorFactory.seed = 0

def detect_lang(text):
    langid_lang, langid_conf = langid.classify(text)

    try:
        langdetect_lang = detect(text)
    except LangDetectException:
        langdetect_lang = "unknown"

    return langid_lang if langid_conf > 0.5 else langdetect_lang

def get_language_name(lang_code):
    try:
        return langcodes.Language.get(lang_code).display_name()
    except:
        return "Unknown"

def slow_typing(text, delay=0.03):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def slow_input(input_text, delay=0.03):
    for char in input_text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    return input()

def continue_or_not():
    while True:
        print(Fore.YELLOW + "Langify: " + Style.RESET_ALL, end="")
        user_input = slow_input("Do you want to continue? (y/n): ")
        if user_input.lower() == "n":
            print(Fore.RED + "Langify: " + Style.RESET_ALL, end="")
            slow_typing("Goodbye!")
            return False
        elif user_input.lower() == "y":
            return True

def chatbot():
    print(Fore.GREEN + "Welcome to Langify! Enter 'exit' to quit." + Style.RESET_ALL)
    while True:
        print(Fore.YELLOW + "Langify: " + Style.RESET_ALL, end="")
        text = slow_input("Enter text you want to be detected: ")
        if text.lower() == "exit":
            print(Fore.RED + "Langify: " + Style.RESET_ALL, end="")
            slow_typing("Goodbye!")
            break
        
        detected_lang_code = detect_lang(text)
        detected_lang_name = get_language_name(detected_lang_code)
        print(Fore.YELLOW + "Langify: " + Style.RESET_ALL, end="")
        slow_typing(f"Detected language: {detected_lang_name}")
        
        if not continue_or_not():
            break

if __name__ == "__main__":
    chatbot()
