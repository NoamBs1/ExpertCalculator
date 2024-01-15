class MathEvaluation:

    @staticmethod
    def add(operand1: float, operand2: float) -> float:
        """
        adding two operands
        :param operand1: float first operand
        :param operand2: float second operand
        :return: the sum of the operands
        """
        return operand1 + operand2

    @staticmethod
    def sub(operand1: float, operand2: float) -> float:
        """
        subtracting operand2 from operand1
        :param operand1: float first operand
        :param operand2: float second operand
        :return: the result of operand1 - operand2
        """
        return operand1 - operand2

    @staticmethod
    def mul(operand1: float, operand2: float) -> float:
        """
        multiplying two operands
        :param operand1: float first operand
        :param operand2: float second operand
        :return: the product of the operands
        """
        return operand1 * operand2

    @staticmethod
    def div(operand1: float, operand2: float) -> float:
        """
        divide operand1 by operand2
        :param operand1: float first operand
        :param operand2: float second operand
        :return: the result of operand1 / operand2
        :raises: ZeroDivisionError if operand2 is 0
        """
        if operand2 != 0:
            return operand1 / operand2
        else:
            raise ZeroDivisionError("can't divide by zero")

    @staticmethod
    def power(operand1: float, operand2: float) -> float:
        """
        operand1 to the power of operand2
        :param operand1: float first operand
        :param operand2: float second operand
        :return: operand1 to the power of operand2
        :raises: ArithmeticError if operand1 is negative and operand 2 is a fraction
        """
        if operand1 == 0 and operand2 <= 0:
            raise ArithmeticError("Math Error")
        if operand1 < 0 and -1 < operand2 < 1:
            raise ArithmeticError("Math Error")
        else:
            try:
                return operand1 ** operand2
            except OverflowError:
                return float('inf')

    @staticmethod
    def mod(operand1: float, operand2: float) -> float:
        """
        calculate the result of operand1 % operand2
        :param operand1: float first operand
        :param operand2: float second operand
        :return: the result of operand1 % operand2
        :raises: ZeroDivisionError if operand2 is 0
        """
        if operand2 != 0:
            return operand1 % operand2
        else:
            raise ZeroDivisionError("can't modulo by zero")

    @staticmethod
    def avg(operand1: float, operand2: float) -> float:
        """
        calculate the average between operand1 and operand2
        :param operand1: float first operand
        :param operand2: float second operand
        :return: the average between operand1 and operand2
        """
        return (operand1 + operand2) / 2

    @staticmethod
    def max(operand1: float, operand2: float) -> float:
        """
        returning the maximum operand between these two operands
        :param operand1: float first operand
        :param operand2: float second operand
        :return: the maximum operand between these two operands
        """
        return operand1 if operand1 > operand2 else operand2

    @staticmethod
    def min(operand1: float, operand2: float) -> float:
        """
        returning the minimum operand between these two operands
        :param operand1: float first operand
        :param operand2: float second operand
        :return: the minimum operand between these two operands
        """
        return operand1 if operand1 < operand2 else operand2

    @staticmethod
    def factorial(operand: float) -> float:
        """
        calculate the factorial of the operand
        :param operand: float operand
        :return: the factorial of the operand
        :raises: ValueError if the operand is negative or not an integer
        """
        if operand < 0:
            raise ValueError("can not be factorized")
        if operand == 0:
            return 1
        if float(operand).is_integer():
            for i in range(int(operand) - 1, 0, -1):
                operand *= i
            return operand
        else:
            raise ValueError("can not be factorized")

    @staticmethod
    def neg(operand: float) -> float:
        """
        change the operand to the other sign
        :param operand: float operand
        :return: -operand (change the sign)
        """
        return -operand

    @staticmethod
    def sumNum(operand: float) -> float:
        """
        summarize all the digits of the operand
        :param operand: float operand
        :return: the sum of all the digits of the operand
        :raises: ValueError if the operand is negatives
        """
        if operand < 0:
            raise ValueError("can not do this on negative number")
        return sum(float(char) for char in str(operand) if char != '.')
