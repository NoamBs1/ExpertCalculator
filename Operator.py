class Operator:
    def __init__(self, char: str, kdimut: int, func, isBinary=True, pos=0):
        self.char = char
        self.kdimut = kdimut
        self.func = func
        self.isBinary = isBinary
        self.pos = pos

    def getKdimut(self):
        return self.kdimut

    def getPosition(self):
        return self.pos
