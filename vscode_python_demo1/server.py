"""Server"""

from typing import List


def echo_string(text: str) -> str:
    return text


def startup(_args: List[str]) -> None:
    print(echo_string("Hello, World!"))
