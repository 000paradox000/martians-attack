from typing import List


def s2m(text: str) -> str:
    """
    Reverses each word in the input string `text` and returns the resulting
    string with words in their original order.

    Args:
        text (str): The input string to be transformed.

    Returns:
        str: The transformed string with each word reversed.
    """
    tokens: List[str] = text.split(" ")
    new_tokens: List[str] = [reverse_string(token) for token in tokens]
    new_text: str = " ".join(new_tokens)
    return new_text


def m2s(text: str) -> str:
    """
    Acts as an alias for the `s2m` function. Reverses each word in the input
    string `text` and returns the resulting string with words in their original
    order.

    Args:
        text (str): The input string to be transformed.

    Returns:
        str: The transformed string with each word reversed.
    """
    return s2m(text)


def reverse_string(text: str) -> str:
    """
    Reverses the input string `text`.

    Args:
        text (str): The input string to be reversed.

    Returns:
        str: The reversed string.
    """
    return text[::-1]
