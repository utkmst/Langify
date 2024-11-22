import langid
from langdetect import detect, DetectorFactory
from langdetect.lang_detect_exception import LangDetectException
from colorama import init, Fore, Style
import langcodes
import sys
import time
from collections import Counter
from polyglot.detect import Detector
from polyglot.detect.base import logger
logger.disabled = True

init(autoreset=True)
DetectorFactory.seed = 0

def extract_char_ngrams(text, n=3):
    """Extract character n-grams from the text."""
    ngrams = [text[i:i+n] for i in range(len(text)-n+1)]
    return Counter(ngrams)

def detect_lang(text):
    langid_lang, langid_conf = langid.classify(text)

    try:
        langdetect_lang = detect(text)
    except LangDetectException:
        langdetect_lang = "unknown"

    try:
        detector = Detector(text)
        polyglot_lang = detector.language.code
    except:
        polyglot_lang = "unknown"
        if polyglot_lang == "unknown":
            print("")

    # Extract character n-grams (trigrams by default)
    char_ngrams = extract_char_ngrams(text)

    # Integrate n-grams into the detection logic
    if langid_conf > 0.5:
        final_lang = langid_lang
    else:
        # Voting mechanism
        votes = [langid_lang, langdetect_lang, polyglot_lang]
        final_lang = max(set(votes), key=votes.count)

    return final_lang

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
