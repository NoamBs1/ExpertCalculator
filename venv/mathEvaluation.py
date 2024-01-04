class MathEvaluation:

    @staticmethod
    def binary_operations(operator, operand1, operand2):
        match operator:
            case '+':
                return MathEvaluation.add(operand1, operand2)
            case '-':
                return MathEvaluation.sub(operand1, operand2)
            case '*':
                return MathEvaluation.mul(operand1, operand2)
            case '/':
                return MathEvaluation.div(operand1, operand2)
            case '%':
                return MathEvaluation.mod(operand1, operand2)
            case '^':
                return MathEvaluation.power(operand1,operand2)
            case '@':
                return MathEvaluation.avg(operand1, operand2)
            case '$':
                return MathEvaluation.max(operand1, operand2)
            case '&':
                return MathEvaluation.min(operand1, operand2)

    @staticmethod
    def unary_operations(operator, operand):
        match operator:
            case '!':
                return MathEvaluation.factorial(operand)
            case '~':
                return MathEvaluation.neg(operand)

    @staticmethod
    def add(operand1, operand2):
        return operand1 + operand2

    @staticmethod
    def sub(operand1, operand2):
        return operand1 - operand2

    @staticmethod
    def mul(operand1, operand2):
        return operand1 * operand2

    @staticmethod
    def div(operand1, operand2):
        if operand2 != 0:
            return operand1 / operand2
        else:
            raise ZeroDivisionError("can't divide by zero")

    @staticmethod
    def power(operand1, operand2):
        return operand1 ** operand2

    @staticmethod
    def mod(operand1, operand2):
        if operand2 != 0:
            return operand1 % operand2
        else:
            raise ZeroDivisionError("can't modulo by zero")

    @staticmethod
    def avg(operand1, operand2):
        return (operand1 + operand2) / 2

    @staticmethod
    def max(operand1, operand2):
        return operand1 if operand1 > operand2 else operand2

    @staticmethod
    def min(operand1, operand2):
        return operand1 if operand1 < operand2 else operand2

    @staticmethod
    def factorial(operand):
        if operand == 0:
            return 1
        if float(operand).is_integer():
            for i in range(int(operand) - 1, 0, -1):
                operand *= i
            return operand
        else:
            raise ValueError("can not be factorized")

    @staticmethod
    def neg(operand):
        return -operand
