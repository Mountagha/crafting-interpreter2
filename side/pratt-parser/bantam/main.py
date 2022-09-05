from lexer import Lexer
from parser import Parser 

if __name__ == "__main__":
    lexer = Lexer("!a")
    parser = Parser(lexer.get_tokens())
    print(parser.parseExpression())