"""Test the server"""

from vscode_python_demo1.server import echo_string


def test_echo_string():
    """Test echo_string"""
    assert echo_string('Hello, World!') == 'Hello, World!'
    foo = echo_string(1)
    print(foo)
