import logging

from libs import utilities
from libs.martian import Martian

logger = logging.getLogger(__name__)


def test_martian_invoke() -> None:
    """Test the Martian's ability to process and respond to queries."""
    spanish_queries = [
        "hola, ¿cómo estás?",
        "me repites tu nombre",
        "¿te sabes algún chiste marciano?",
    ]
    martian = Martian()

    logger.debug("=" * 50)

    for idx, spanish_query in enumerate(spanish_queries):
        if idx > 0:
            logger.debug("-" * 50)

        martian_query = utilities.s2m(spanish_query)
        martian_response = martian.invoke(martian_query)
        spanish_response = utilities.m2s(martian_response)

        logger.debug(
            f"\nQuery: {spanish_query}\n\nResponse:\n{spanish_response}"
        )

        # Check if the conversion back to Spanish is correct
        assert spanish_response == utilities.m2s(
            martian_response
        ), f"Assertion failed for query: {spanish_query}"
