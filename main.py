import logging

from libs.translator import Translator
from libs.tts import TTS

logger = logging.getLogger(__name__)


class Handler:
    def __init__(self):
        self.translator = Translator()
        self.tts = TTS()

    def start(self):
        self.invoke(query="hola", print_output=True)
        logger.debug("=" * 50)
        self.invoke(query="eres alérgico a algún alimento?", print_output=True)
        logger.debug("=" * 50)
        self.invoke(query="hola", print_output=True)
        logger.debug("=" * 50)
        self.invoke(query="eres alérgico a algún alimento?", print_output=True)

    def stop(self):
        self.tts.stop()

    def invoke(
        self, query: str, speak: bool = False, print_output: bool = False
    ) -> str:
        output = f"User Query:\n{query}"
        logger.debug(output)
        response = self.translator.invoke(query)

        if print_output:
            output = f"Query:\n{query}\n\nResponse:\n{response}"
            logger.debug(output)

        if speak:
            self.tts.speak(response)

        return response


def main():
    handler = Handler()
    handler.start()
    handler.stop()


if __name__ == "__main__":
    main()
