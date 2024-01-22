<<<<<<< HEAD
class Operator:
    def __init__(self, char: str, kdimut: int, func, isBinary=True, pos=0):
        """
        Initialize a new Operator
        :param char: str char - the operator
        :param kdimut: int priority in order of operations
        :param func: the function that it operates
        :param isBinary: boolean if the operator is binary
        :param pos: the position of the operator relative to the location of the operand
        """
        self.char = char
        self.kdimut = kdimut
        self.func = func
        self.isBinary = isBinary
        self.pos = pos

    def getKdimut(self) -> int:
        """
        returns the priority of the operator
        :return: the priority of the operator
        """
        return self.kdimut

    def getPosition(self) -> int:
        """
        return the position of the operator relative to the location of the operand
        :return: the position of the operator relative to the location of the operand
        """
        return self.pos

