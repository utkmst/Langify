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
import json
import argparse

logger.disabled = True

init(autoreset=True)
DetectorFactory.seed = 0

# Load translations
with open('localization.json', 'r') as f:
    translations = json.load(f)

def get_translation(key, lang='en'):
    return translations.get(lang, {}).get(key, key)

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

    # Extract character n-grams (trigrams by default)
    char_ngrams = extract_char_ngrams(text)

    # Integrate n-grams into the detection logic
    if langid_conf > 0.5:
        final_lang = langid_lang
    else:
        # Voting mechanism
        votes = [langid_lang, langdetect_lang, polyglot_lang]
        final_lang = max(set(votes), key=votes.count)

    if final_lang == "unknown" and langid_lang == "unknown" and langdetect_lang == "unknown" and polyglot_lang == "unknown":
        print("Detector is not able to detect the language reliably.")

    return {
        "final_lang": final_lang,
        "langid_lang": langid_lang,
        "langdetect_lang": langdetect_lang,
        "polyglot_lang": polyglot_lang
    }

def get_language_name(lang_code, user_lang='en'):
    try:
        return langcodes.Language.get(lang_code).display_name(user_lang)
    except:
        return "Unknown"

def slow_typing(text, delay=0.03):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def slow_input(input_text, delay=0.03, end='\n'):
    for char in input_text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    return input()

def continue_or_not(user_lang):
    while True:
        print(Fore.YELLOW + "Langify: " + Style.RESET_ALL, end="")
        user_input = slow_input(get_translation('continue', user_lang))
        if user_input.lower() == "n" or user_input.lower() == "h":
            print(Fore.RED + "Langify: " + Style.RESET_ALL, end="")
            slow_typing(get_translation('goodbye', user_lang))
            return False
        elif user_input.lower() == "y" or user_input.lower() == "e":
            return True

def main():
    parser = argparse.ArgumentParser(description="Langify - Language Detection Tool")
    parser.add_argument('--lang', type=str, default='en', help='select_language')
    args = parser.parse_args()

    user_lang = args.lang
    print(Fore.YELLOW + "Langify: " + Style.RESET_ALL, end="")
    user_lang = slow_input(get_translation('select_language', user_lang))
    print(Fore.YELLOW + "Langify: " + Style.RESET_ALL, end="")
    slow_typing(get_translation('welcome', user_lang))

    while True:
        print(Fore.YELLOW + "Langify: " + Style.RESET_ALL, end="")
        text = slow_input(get_translation('enter_text', user_lang))
        if text.lower() == 'exit':
            print(Fore.YELLOW + "Langify: " + Style.RESET_ALL, end="")
            slow_typing(get_translation('goodbye', user_lang))
            break

        if text.lower() == 'summary':
            print(Fore.YELLOW + "Langify: " + Style.RESET_ALL, end="")
            slow_typing(get_translation('enter_text', user_lang), end="")
            text = slow_input("")
            detection_result = detect_lang(text)
            final_lang = detection_result["final_lang"]
            langid_lang = detection_result["langid_lang"]
            langdetect_lang = detection_result["langdetect_lang"]
            polyglot_lang = detection_result["polyglot_lang"]

            print(Fore.YELLOW + "Langify: " + Style.RESET_ALL, end="")
            slow_typing(f"{get_translation('detected_language', user_lang)} {get_language_name(final_lang, user_lang)}")

            print(Fore.YELLOW + "Langify: " + Style.RESET_ALL, end="")
            slow_typing(get_translation('summary', user_lang))
            slow_typing(f"  final: {get_language_name(final_lang, user_lang)}")
            slow_typing(f"  langid: {get_language_name(langid_lang, user_lang)}")
            slow_typing(f"  langdetect: {get_language_name(langdetect_lang, user_lang)}")
            slow_typing(f"  polyglot: {get_language_name(polyglot_lang, user_lang)}")
        else:
            detection_result = detect_lang(text)
            final_lang = detection_result["final_lang"]

            print(Fore.YELLOW + "Langify: " + Style.RESET_ALL, end="")
            slow_typing(f"{get_translation('detected_language', user_lang)} {get_language_name(final_lang, user_lang)}")

        if not continue_or_not(user_lang):
            break

if __name__ == "__main__":
    main()