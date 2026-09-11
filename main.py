import sys

from lexer import Lexer
from parser_ import Parser
from interpreter import Interpreter

while True:
    try:
        text = input("Calc: ")
        lexer = Lexer(text)
        tokens = lexer.generate_tokens()
        parser = Parser(tokens)
        tree = parser.parse()
        if not tree:
            continue

        interpreter = Interpreter()
        value = interpreter.visit(tree)
        print(value)
    except KeyboardInterrupt:
        print()
        sys.exit(0)
    except Exception as err:
        print(err)