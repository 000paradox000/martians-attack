import logging

from libs.translator import Translator

logger = logging.getLogger(__name__)


def test_translator_invoke() -> None:
    """Test the translator's ability to process and respond to queries."""
    spanish_queries = [
        "hola, ¿cómo estás?",
        "me repites tu nombre",
        "¿te sabes algún chiste marciano?",
    ]
    translator = Translator()

    logger.debug("=" * 50)

    for idx, spanish_query in enumerate(spanish_queries):
        if idx > 0:
            logger.debug("-" * 50)

        spanish_response = translator.invoke(spanish_query)

        logger.debug(
            f"\nQuery: {spanish_query}\n\nResponse:\n{spanish_response}"
        )
