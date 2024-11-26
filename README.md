
![Alt text](https://camo.githubusercontent.com/445e08dc4241e9b0373c6179fdb8aa0b29fd063eef17541b8f0d8c49aa0072d9/68747470733a2f2f692e6962622e636f2f546858446e62522f4c656f6e6172646f2d50686f656e69782d412d7374796c697a65642d6c6f676f2d666561747572696e672d612d676c6f62652d656d6f6a692d7365742d612d322d72656d6f766562672d707265766965772e706e67)


# Langify: Language Detection Chatbot 🗣️🌍

Langify is a Python-based chatbot that detects the language of input text using multiple language detection libraries and techniques. It combines the results from libraries like `langid`, `langdetect`, and `polyglot` to provide a robust language detection mechanism. The chatbot offers an engaging user experience with slow typing effects and the option to continue or exit the session.

---

## Features

- **Multi-library Detection**: Integrates `langid`, `langdetect`, and `polyglot` for accurate language detection.
- **Localization Support**: Uses a `localization.json` file for multilingual chatbot responses. Users can select their preferred language at the start of the session.
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

## Usage

1. **Clone the repository**:

   ```bash
   git clone https://github.com/utkmst/Langify.git
   cd Langify
   ```

2. **Run the chatbot**:

   ```bash
   python Langify.py
   or
   python Langify.py --lang 'code of the language you want it to be continue with'
   ```

3. **Interact with Langify**:
   - Enter text to detect its language.
   - Respond to prompts to continue or exit the session.
   - Type `exit` to quit the chatbot.
   - Type `summary` if you want a summary of detected languages by models.

---
## Languages that Supported in Interface:
![Alt text](https://camo.githubusercontent.com/8548b13d042708a4b1dc471fc1a234d6b883b37bbddbb160315ca0690d89edb0/68747470733a2f2f692e6962622e636f2f3573475750374e2f696d6167652e706e67)

   -🇬🇧English
   
   -🇨🇳Chinese
   
   -🇪🇸Spanish
   
   -🇷🇺Russian
   
   -🇯🇵Japanese
   
   -🇰🇷Korean
   
   -🇹🇷Turkish
   
   -🇩🇪German
   
   -🇫🇷French
   
   -🇮🇩Indonesian
   
   -🇵🇹Portugal
   
   -🇷🇸Serbian
   
   -🇲🇰Macedonian
   
   -🇬🇷Greek

   -🇮🇹Italian

   -🇳🇱Dutch

## Example Interaction

```plaintext
Langify: Please select your language (default: en): en
Langify: Welcome to Langify! Enter 'exit' to quit.
Langify: Enter text you want to be detected: Bonjour, comment ça va ?
Langify: Detected language: French
Langify: Do you want to continue? (y/n): y
Langify: Enter text you want to be detected: これは日本語のサンプルです
Langify: Detected language: Japanese
Langify: Do you want to continue? (y/n): n
Langify: Goodbye!
```

---

## How It Works

1. **Language Detection**:
   - Detects the language using three libraries:
     - `langid` provides a language code and confidence score.
     - `langdetect` detects the language or returns `unknown` if detection fails.
     - `polyglot` uses statistical models for language detection.
   - Implements a **voting mechanism** to resolve conflicts between libraries.

2. **Localization**:
   - Prompts and responses are translated based on the user's language selection.
   - Uses a JSON file (localization.json) to store translations for multiple languages.

3. **Character n-grams**:
   - Extracts and analyzes sequences of characters (e.g., trigrams) for additional language features.

4. **Interactive Experience**:
   - Provides slow-typing effects for prompts and responses.
   - Allows users to choose whether to continue after each detection.

---

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

---

## Acknowledgements

- [Langid](https://github.com/saffsd/langid.py)
- [Langdetect](https://github.com/Mimino666/langdetect)
- [Polyglot](https://polyglot.readthedocs.io/)
- [Colorama](https://pypi.org/project/colorama/)
- [Langcodes](https://pypi.org/project/langcodes/)

---

Enjoy using **Langify** to explore languages from around the world in your preffered language! 🌍✨


