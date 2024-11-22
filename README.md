# Langify: Language Detection Chatbot 🗣️🌍

Langify is a Python-based chatbot that detects the language of input text using multiple language detection libraries and techniques. It combines the results from libraries like `langid`, `langdetect`, and `polyglot` to provide a robust language detection mechanism. The chatbot offers an engaging user experience with slow typing effects and the option to continue or exit the session.

---

## Features

- **Multi-library Detection**: Integrates `langid`, `langdetect`, and `polyglot` for accurate language detection.
- **Character n-gram Analysis**: Uses trigrams (or customizable n-grams) to analyze text characteristics.
- **Interactive Chatbot Interface**: Engages users with slow-typing effects using the `colorama` library for colored prompts.
- **Language Name Lookup**: Converts detected language codes to human-readable names using `langcodes`.
- **Flexible Exit Option**: Allows users to exit the session or continue with more text inputs.

---

## Requirements

This project requires Python 3.6 or higher and the following Python libraries:

- `langid`
- `langdetect`
- `polyglot`
- `colorama`
- `langcodes`

You can install all dependencies with the following command:

```bash
pip install langid langdetect polyglot colorama langcodes
