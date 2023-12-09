import requests


class ReversoTranslateError(Exception):
    """
    Exception raised for errors occurring during Reverso translation.
    """

    def __init__(self):
        """
        Initialize the ReversoTranslateError.
        """
        super().__init__("An error has occurred, you probably didn't specify a translation language.")


class ReversoTranslator:
    """
    A class to interact with the Reverso translation API.
    """

    def __init__(self) -> None:
        """
        Initialize the ReversoTranslator class.
        """
        self._url = "https://api.reverso.net/translate/v1/translation"
        self._language_detection: bool = False
        self._language_from = "eng"
        self._language_to = "fra"
        self._input = ""
        self._session = requests.Session()
        self._session.headers.update({
            'Accept': 'application/json, text/plain, */*',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'fr,fr-FR;q=0.8,en-US;q=0.5,en;q=0.3',
            'Connection': 'keep-alive',
            'Content-Type': 'application/json',
            'Host': 'api.reverso.net',
            'Origin': 'https://www.reverso.net',
            'Referer': 'https://www.reverso.net/',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-site',
            'TE': 'trailers',
            'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/118.0',
            'X-Reverso-Origin': 'translation.web'
        })
        self._payload = {
            "format": "text",
            "from": "",
            "to": "",
            "input": "Default Settings",
            "options": {
                "languageDetection": False,
                "sentenceSplitter": True,
                "origin": "translation.web",
                "contextResults": True
            }
        }

    def set_language_from(self, language: str):
        """
        Set the source language for translation.

        Args:
            language (str): The language code (e.g., 'eng' for English).

        Returns:
            ReversoTranslator: The ReversoTranslator instance.
        """
        self._language_from = language
        self._payload["from"] = self._language_from
        return self

    def set_language_to(self, language: str):
        """
        Set the target language for translation.

        Args:
            language (str): The language code (e.g., 'fra' for French).

        Returns:
            ReversoTranslator: The ReversoTranslator instance.
        """
        self._language_to = language
        self._payload["to"] = self._language_to
        return self

    def set_language_detection(self, value: bool):
        """
        Enable or disable language detection.

        Args:
            value (bool): True to enable, False to disable.

        Returns:
            ReversoTranslator: The ReversoTranslator instance.
        """
        self._language_detection = value
        self._payload["options"]["languageDetection"] = self._language_detection
        return self

    def translate(self, input_text: str):
        """
        Translate the given input text.

        Args:
            input_text (str): The text to translate.

        Returns:
            str: The translated text.

        Raises:
            ReversoTranslateError: If an error occurs during translation.
        """
        self._input = input_text
        self._payload["input"] = input_text
        response = self._session.post(url=self._url, json=self._payload)

        try:
            translated_text = response.json()['translation'][0]
        except KeyError:
            raise ReversoTranslateError

        return translated_text



