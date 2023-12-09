---

# Python Unofficial Reverso API 

A Python unofficial api for Reverso

## Introduction

This Python API allows seamless interaction with the Reverso translation API, enabling translation between different languages.

## Installation

To use this API, ensure you have Python installed. Clone this repository and place the `reverso_translator.py` file in your project directory.

## Requirements

Ensure you have the following dependencies installed:

- **Python** - Ensure you have Python installed on your system.
- **Requests** - This project relies on the `requests` library for handling HTTP requests. Install it via pip:
  ```
  pip install requests
  ```



## Usage

### Example

```python
from reverso_translator import ReversoTranslator

translator = ReversoTranslator()
translation = translator.set_language_from("fra").set_language_to("eng")
translated_text = translation.translate("Salut, ça va ?")
print(translated_text)
```

### Methods

#### `set_language_from(language: str)`

Set the source language for translation.

#### `set_language_to(language: str)`

Set the target language for translation.

#### `set_language_detection(value: bool)`

Enable or disable language detection.

#### `translate(input_text: str)`

Translate the given input text.

### Error Handling

This API raises a `ReversoTranslateError` if an error occurs during translation. Ensure to handle this exception in your code.

## Contributions

Contributions are welcome! Feel free to fork this repository, make changes, and submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).

---
