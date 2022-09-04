from curses.ascii import isalnum
from token_type import TokenType

class Lexer: 
    def __init__(self, mText: str) -> None:
        self.mPunctuators = [] # list of tuples
        self.mText = mText
        self.index = 0 # to go through the text.

    def get_token_name(self):
        identifer = ""
        while True:
            if self.mText[self.index] == " " or len(self.mText) == self.index - 1:
                break
            identifer += self.mText[self.index]
            self.index += 1

    def tokenize(self):
        while True:
            if self.index - 1 == len(self.mText):
                break # end of file 
            char = self.mText[self.index]
            self.index += 1
            if char == '(':
                self.mPunctuators.append((TokenType.LEFT_PAREN, char))
            elif char == ')':
                self.mPunctuators.append((TokenType.RIGHT_PAREN, char))
            elif char == ',':
                self.mPunctuators.append((TokenType.COMMA, char))
            elif char == '=':
                self.mPunctuators.append((TokenType.ASSIGN, char)) 
            elif char == '+':
                self.mPunctuators.append((TokenType.PLUS, char))
            elif char == '-':
                self.mPunctuators.append((TokenType.MINUS, char))
            elif char == '*':
                self.mPunctuators.append((TokenType.ASTERIK, char))
            elif char == '/':
                self.mPunctuators.append((TokenType.SLASH, char))
            elif char == '^':
                self.mPunctuators.append((TokenType.CARET, char))
            elif char == '~':
                self.mPunctuators.append((TokenType.TILDE, char))
            elif char == '!':
                self.mPunctuators.append((TokenType.BANG, char)) 
            elif char == '?':
                self.mPunctuators.append((TokenType.QUESTION, char))
            elif char == ':':
                self.mPunctuators.append((TokenType.COLON, char))
            elif isalnum(char):
                self.get_token_name()
            else:
                continue # ignore all other char

        self.mPunctuators.append((TokenType.EOF, None))
    def get_token(self):
        return self.mPunctuators
    
if __name__ == "__main__":
    source = "a = 1 + 2" 
    lexer = Lexer(source)
    lexer.tokenize()
    print(lexer.get_token())
            