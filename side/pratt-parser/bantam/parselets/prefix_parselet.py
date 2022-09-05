
from expressions.expression import Expression, PrefixExpression, NameExpression
from parser import Parser
from token import Token
"""
One of the two interfaces used by the Pratt parser. A PrefixParselet is 
associated with a token that appears at the beginning of an expression. Its
parse() method will be called with the consumed leading token, and the 
parselet is responsible for parsing anything that comes after that token.
this interface is also used for single-token expressions like variables, in
which case parse() simply doesn't consume any more tokens
original @author: rnystrom. Rewritten by @Mountagha 
"""

class PrefixParselet:
    def parse(parser: Parser, token: Token) -> Expression:
        pass

"""
Generic prefix parselet for an unary arithmetic operator. Parses prefix
unary "-", "+", "~", "!" expressions.
"""

class PrefixOperatorParselet(PrefixParselet):
    def __init__(self, precedence: int) -> None:
        super().__init__()
        self.mPrecedence = precedence

    @property
    def precedence(self):
        return self.mPrecedence
    
    def parse(self, parser: Parser, token: Token) -> Expression:
        """
        To handle right-associative operators like "^", we allow a slightly 
        lower precedence when parsing the right hand side. this will let
        a parselet with the same precedence appear on the right, which will
        then take *this* parselet's result as its left-hand argument.
        """ 
        right = parser.parseExpression(self.mPrecedence)
        return PrefixExpression(token.mtype, right)

    
class NameParselet(Expression):
    """
    Simple parselet for a named variable like "abc".
    """
    def __init__(self) -> None:
        super().__init__()
    
    def parse(self, parser: Parser, token: Token) -> Expression:
        return NameExpression(token.mtype) 


