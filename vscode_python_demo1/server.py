"""Server"""

from typing import List


def echo_string(text: str) -> str:
    """Echo the input argument

    Args:
        text (str): Some text

    Returns:
        str: The text provided
    """
    return text


def startup(_args: List[str]) -> None:
    """Start the server

    Args:
        _args (List[str]): The command l;ine arguments.
    """
    print(echo_string("Hello, World!"))
