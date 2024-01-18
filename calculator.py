from nis import *
from Operator import Operator
from mathEvaluation import MathEvaluation


class ExpertCalculator:
    OPERATORS = {
        '+': Operator('+', 1, MathEvaluation.add),
        '-': Operator('-', 1, MathEvaluation.sub),
        '*': Operator('*', 2, MathEvaluation.mul),
        '/': Operator('/', 2, MathEvaluation.div),
        '^': Operator('^', 3, MathEvaluation.power),
        '%': Operator('%', 4, MathEvaluation.mod),
        '@': Operator('@', 5, MathEvaluation.avg),
        '$': Operator('$', 5, MathEvaluation.max),
        '&': Operator('&', 5, MathEvaluation.min),
        '!': Operator('!', 6, MathEvaluation.factorial, False, POST),
        '~': Operator('~', 6, MathEvaluation.neg, False, PRE),
        '#': Operator('#', 6, MathEvaluation.sumNum, False, POST)
    }

    def __init__(self):
        self.algo = Algorithm(self.OPERATORS)

    def calculate(self):
        try:
            value = self.algo.calculate_expression()
            return value
        except (ValueError, EOFError, ArithmeticError, OverflowError) as err:
            return str(err)


def main():
    calculator = ExpertCalculator()
    result = calculator.calculate()
    print(result)


if __name__ == '__main__':
    main()
