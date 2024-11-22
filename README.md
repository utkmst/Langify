
![Alt text](https://i.ibb.co/ThXDnbR/Leonardo-Phoenix-A-stylized-logo-featuring-a-globe-emoji-set-a-2-removebg-preview.png)


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

## Usage

1. **Clone the repository**:

   ```bash
   git clone https://github.com/your-username/langify.git
   cd langify
   ```

2. **Run the chatbot**:

   ```bash
   python langify.py
   ```

3. **Interact with Langify**:
   - Enter text to detect its language.
   - Respond to prompts to continue or exit the session.
   - Type `exit` to quit the chatbot.

---

## Example Interaction

```plaintext
Welcome to Langify! Enter 'exit' to quit.
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

2. **Character n-grams**:
   - Extracts and analyzes sequences of characters (e.g., trigrams) for additional language features.

3. **Interactive Experience**:
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

Enjoy using **Langify** to explore languages from around the world! 🌍✨


