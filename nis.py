from mathEvaluation import MathEvaluation
from Operator import Operator

POST = 1
PRE = -1


class Algorithm:

    def __init__(self, operators: dict):
        """
        Initialize all the given operators as an attribute, and define attributes due to the given operators
        :param operators: dictionary of operators that the algorithm work according to them
        """
        self.operators = operators
        self.UNARYS = [op for op in self.operators if not self.operators[op].isBinary]
        self.POSTFIX_UNARYS = [op for op in self.operators if self.operators[op].getPosition() == 1]
        self.PREFIX_UNARYS = [op for op in self.operators if self.operators[op].getPosition() == -1]
        self.MINUS_UNARY = 'N'
        self.operators[self.MINUS_UNARY] = Operator('N', 7, MathEvaluation.neg, False, PRE)
        self.PRE_MINUS_UNARY = ['^', '!', '$', '@', '&', '%', '#']

    @staticmethod
    def is_numeric(token: str) -> bool:
        """
        checks if the token can be converted to a number
        :param token: a str
        :return: boolean answer
        """
        try:
            float(token)
            return True
        except ValueError:
            return False

    def is_higher(self, stack: list, op1: str, op2: str) -> bool:
        """
        checks which operator is with the higher priority in order of operations
        :param stack: the stack that represent the priorities
        :param op1: str first operator
        :param op2: str second operator
        :return: True if op1 is in high priority than op2, else False
        """
        if len(stack) == 1 and op1 == self.MINUS_UNARY and op2 in self.PRE_MINUS_UNARY:
            return False
        if len(stack) >= 2 and stack[-2] == '(' and op1 == self.MINUS_UNARY and op2 in self.PRE_MINUS_UNARY:
            return False
        if self.operators[op1].getKdimut() >= self.operators[op2].getKdimut():
            return True
        return False

    def infix_to_postfix(self, expression: list) -> list:
        """
        converting infix expression to postfix expression
        :param expression: list of tokens in infix expression
        :return: list of tokens in postfix expression according to the infix expression
        :raises: ValueError if the parentheses in the expression are not matching
        """
        postfix = []
        stack = []

        for token in expression:
            if token == '':
                raise ValueError("you used the - sign in a wrong way")
            elif Algorithm.is_numeric(token):
                postfix.append(token)
            elif token == '(':
                stack.append(token)
            elif token == ')':
                while stack and stack[-1] != '(':
                    postfix.append(stack.pop())
                if stack:
                    stack.pop()
                else:
                    raise ValueError("not matching parentheses")
            else:
                while stack and stack[-1] != '(' and self.is_higher(stack, stack[-1], token):
                    postfix.append(stack.pop())
                stack.append(token)

        if '(' in stack or ')' in stack:
            raise ValueError("not matching parentheses")
        while stack:
            postfix.append(stack.pop())

        return postfix

    @staticmethod
    def convert_to_numbers(postfix_expression: list):
        """
        converts all the actual numbers to float in a list.
        :param postfix_expression: list of tokens that represent the postfix expression
        """
        for i in range(len(postfix_expression)):
            if Algorithm.is_numeric(postfix_expression[i]):
                postfix_expression[i] = float(postfix_expression[i])

    def tokenize_expression(self, expression: str) -> list:
        """
        converts a string to a list of tokens
        :param expression: str expression
        :return: a list of tokens that represent the actual expression
        :raises: ValueError if the expression that was given is not valid according to the required rules
        """

        if expression == '':
            raise ValueError("you need to enter something")
        tokens = []
        current_token = ''

        for i, char in enumerate(expression):
            if char == self.MINUS_UNARY:
                raise ValueError(f"Invalid character: {self.MINUS_UNARY}")
            elif char.isdigit() or (char == '.' and current_token and '.' not in current_token):
                current_token += char
            elif char == '(' and expression[i + 1] == ')':
                raise ValueError("can not get empty parentheses")
            elif ((char in self.operators or char in ['(', ')']) and
                  char not in self.UNARYS + ['-']):
                if current_token:
                    tokens.append(current_token)
                    current_token = ''
                tokens.append(char)
            elif char == '-':
                if i == 0 or (expression[i - 1] in self.operators and expression[i - 1] not in self.POSTFIX_UNARYS) or \
                        expression[i - 1] == '(':
                    current_token += char
                else:
                    if current_token:
                        tokens.append(current_token)
                        current_token = ''
                    tokens.append(char)
            elif char in self.POSTFIX_UNARYS:
                if i + 1 < len(expression) and (Algorithm.is_numeric(expression[i + 1]) or expression[i + 1] == '('):
                    raise ValueError(f"{char} should not be followed by a number")
                else:
                    if current_token:
                        tokens.append(current_token)
                        current_token = ''
                    tokens.append(char)
            elif char in self.PREFIX_UNARYS:
                if i - 1 > -1 and (Algorithm.is_numeric(expression[i - 1]) or expression[i - 1] == ')'
                                   or expression[i - 1] in self.POSTFIX_UNARYS):
                    raise ValueError(f"{char} should not be preceded by a number")
                else:
                    if current_token:
                        tokens.append(current_token)
                        current_token = ''
                    tokens.append(char)
            else:
                raise ValueError(f"Invalid character: {char}")

        if current_token:
            tokens.append(current_token)

        for i in range(len(tokens)):
            token = tokens[i]
            if token.count('-') > 1:
                rep = token.count('-') * '-'
                if token.count('-') % 2 == 0:
                    tokens[i] = token.replace(rep, '')
                else:
                    tokens[i] = token.replace(rep, '-')

        for i in range(len(tokens)):
            token = tokens[i]
            if token.startswith('-') and Algorithm.is_numeric(token[1:]):
                tokens.insert(i, self.MINUS_UNARY)
                tokens[i + 1] = tokens[i + 1].replace('-', '')
            elif token == '-' and (tokens[i - 1] not in "0123456789)" and tokens[i - 1] not in self.POSTFIX_UNARYS):
                tokens[i] = self.MINUS_UNARY

        print(tokens)
        return tokens

    def calculate_expression(self, expression: str) -> float:
        """
        the main algorithm that calculates the expression
        :param expression: a str that represents the expression required for the calculation
        :return: the arithmetic result of the expression
        :raises: ValueError if the expression was not valid
        """
        stack = []
        postfix_expression = self.infix_to_postfix(self.tokenize_expression(expression))
        Algorithm.convert_to_numbers(postfix_expression)

        for token in postfix_expression:
            if isinstance(token, float):
                stack.append(token)
            else:
                operator = self.operators[token]
                if not operator.isBinary:
                    if not stack:
                        raise ValueError("not valid")
                    operand = stack.pop()
                    value = operator.func(operand)
                    stack.append(value)
                else:
                    if len(stack) < 2:
                        raise ValueError("not valid")
                    operand2 = stack.pop()
                    operand1 = stack.pop()
                    value = operator.func(operand1, operand2)
                    stack.append(value)

        result = stack.pop()
        if len(stack) != 0:
            raise ValueError("not a valid input")
        else:
            if float(result).is_integer():
                return int(result)
            return result
