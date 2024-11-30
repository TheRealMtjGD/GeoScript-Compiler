class ParserObject:
    def __init__(self) -> None:
        self.opcode = 'undefined'
        self.operand = {}
    
    def define_opcode(self, _Opcode: str) -> None:
        self.opcode = _Opcode
    
    def define_operand(self, _Operand: dict) -> None:
        self.operand = _Operand