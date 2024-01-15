from nis import *
from Operator import Operator
from mathEvaluation import MathEvaluation
from input import getStr


def ExpertCalculator():
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

    try:
        algo = Algorithm(OPERATORS)
        expression = getStr()
        value = algo.calculate_expression(expression)
    except (ValueError, EOFError, ArithmeticError, KeyboardInterrupt) as err:
        print(err)
    else:
        print(value)


def main():
    ExpertCalculator()


if __name__ == '__main__':
    main()
