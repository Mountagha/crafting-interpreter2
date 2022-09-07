
from token_type import TokenType

class Expression:
    pass


class NameExpression(Expression):
    def __init__(self, name: str) -> None:
        super().__init__()
        self.mName = name
    
    @property
    def name(self):
        return self.mName
    
    def __repr__(self) -> str:
        return self.mName


class PrefixExpression(Expression):
    def __init__(self, operator: TokenType, right: Expression) -> None:
        super().__init__()
        self.mOperator = operator
        self.mRight = right
    
    def __repr__(self) -> str:
        return f"( {str(self.mOperator)} {self.mRight.__repr__()} )"
    

