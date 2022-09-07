from parselets.prefix_parselet import NameParselet, PrefixOperatorParselet 
from token_type import TokenType
from lexer import Lexer
from parser import Parser
"""
Extends the generic Parser class with support for parsing the actual
bantam grammar.
"""
class BantamParser(Parser):
    def __init__(self, tokens) -> None:
        super().__init__(tokens)

        # Register all of the parselets for the grammar.

        # Register the ones that need special parselets
        super().register(TokenType.NAME, NameParselet())

        # Register the simple operator parselets
        super().register(TokenType.BANG, PrefixOperatorParselet(1)) # testing purposes.