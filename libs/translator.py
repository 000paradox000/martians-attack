import logging

from langchain.chat_models import init_chat_model
from langchain_core.messages import HumanMessage, SystemMessage

from libs import utilities
from libs.martian import Martian
from .messages import TRANSLATOR_BASE_SYSTEM_MESSAGE

logger = logging.getLogger(__name__)


class Translator:
    def __init__(self):
        self._llm = None
        self.martian = Martian()
        self._new_knowledge = []
        self._base_knowledge = [
            {
                "español": "hola",
                "marciano": "aloh",
            },
            {
                "español": "hola, ¿cómo estás?",
                "marciano": "?sátse omóc¿ ,aloh",
            },
        ]

    def invoke(self, spanish_query: str) -> str:
        return self._invoke(spanish_query)

    def _invoke(self, text: str) -> str:
        logger.debug(f"System Message: {self.system_message}")

        messages = [
            SystemMessage(self.system_message),
            HumanMessage(text),
        ]

        response = self.llm.invoke(messages).content
        logger.debug(f"Translator response: {response}")

        if not self._is_success(response):
            response = self.learn(text)
            logger.debug(f"Learn response: {response}")
            response = self.martian.invoke(response)
            response = self.translate_martian_response(response)
        else:
            # TODO tweak spanish
            pass

        return response

    def translate_martian_response(self, martian_response: str) -> str:
        return utilities.m2s(martian_response)

    def _is_success(self, response: str):
        response = response.lower()
        response = response.strip()

        options = [
            "no lo se",
            "no lo sé",
        ]

        return all(option not in response for option in options)

    @property
    def system_message(self) -> str:
        msg = TRANSLATOR_BASE_SYSTEM_MESSAGE
        msg += "translations: [\n"
        msg += self.knowledge
        msg += "\n]"

        return msg

    @property
    def knowledge(self) -> str:
        elements = self._base_knowledge + self._new_knowledge
        output = ""
        for idx, element in enumerate(elements):
            if idx > 0:
                output += ",\n"
            output += "    " + str(element)

        return output

    @property
    def model_name(self):
        return "llama3.2:1b"

    @property
    def llm(self):
        if not self._llm:
            self._llm = init_chat_model(
                self.model_name,
                model_provider="ollama",
                temperature=0.1,
            )

        return self._llm

    def learn(self, text: str):
        # TODO
        # Implement a learning method
        response = utilities.s2m(text)
        item = {
            "español": text,
            "marciano": response,
        }

        if item in self._new_knowledge:
            return response

        self._new_knowledge.append(
            {
                "español": text,
                "marciano": response,
            }
        )

        return response
