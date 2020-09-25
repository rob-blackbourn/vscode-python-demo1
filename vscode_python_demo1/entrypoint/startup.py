"""Entry point for server"""

import sys

from vscode_python_demo1 import startup


def main():
    """Start the server"""

    startup(sys.argv)


if __name__ == '__main__':
    main()
