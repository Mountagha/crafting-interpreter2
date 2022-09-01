from enum import Enum
from lib2to3.pgen2.token import COLON, SLASH, TILDE
from tkinter import W

class TokenType(Enum):
    LEFT_PAREN=1,
    RIGHT_PAREN=2,
    COMMA=3,
    ASSIGN=4,
    PLUS=5,
    MINUS=6,
    ASTERIK=7,
    SLASH=8,
    CARET=9,
    TILDE=10,
    BANG=11,
    QUESTION=12,
    COLON=13,
    NAME=14,
    EOF=15

    # If the tokenType represents a punctuator (i.e a token that can split an
    # identifier like '+', this will get its text.)
    
    def punctuator(self):
        pass


class Lexer: 
    def __init__(self, mText: str) -> None:
        self.mPunctuators = {}
        self.mText = mText
    def other(self):
        pass
        