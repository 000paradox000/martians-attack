from langchain.chat_models import init_chat_model
from langchain_core.messages import HumanMessage, SystemMessage

from libs import utilities
from libs.messages import MARTIAN_SYSTEM_MESSAGE


class Martian:
    """
    A class to simulate a Martian named Zort, who interacts with humans by
    translating queries into a fictional Martian language and vice versa.

    Attributes:
        _llm: An instance of a language model used for generating responses.
    """

    def __init__(self) -> None:
        """
        Initializes the Martian with no language model loaded initially.
        """
        self._llm = None

    def invoke(self, martian_query: str) -> str:
        """
        Translates a query from Martian to Spanish, invokes the language model
        to get a response, and then translates the response back to Martian.

        Args:
            martian_query (str): The query in Martian language.

        Returns:
            str: The response in Martian language.
        """
        spanish_query = utilities.m2s(martian_query)
        spanish_response = self._invoke(spanish_query)
        martian_response = utilities.s2m(spanish_response)
        return martian_response

    def _invoke(self, text: str) -> str:
        """
        Sends the translated Spanish query to the language model and receives
        a response.

        Args:
            text (str): The query in Spanish.

        Returns:
            str: The response from the language model in Spanish.
        """
        messages = [
            SystemMessage(self.system_message),
            HumanMessage(text),
        ]
        return self.llm.invoke(messages).content

    @property
    def system_message(self) -> str:
        """
        Provides a system message that describes the personality and role of
        the Martian character.

        Returns:
            str: A descriptive system message.
        """
        return MARTIAN_SYSTEM_MESSAGE

    @property
    def model_name(self) -> str:
        """
        Specifies the name of the language model to be used.

        Returns:
            str: The name of the language model.
        """
        return "llama3.2:1b"

    @property
    def llm(self):
        """
        Lazily initializes and returns the language model instance.

        Returns:
            An instance of the language model.
        """
        if not self._llm:
            self._llm = init_chat_model(
                self.model_name,
                model_provider="ollama",
                temperature=0.9,
            )
        return self._llm
