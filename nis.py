from inputChecks import *
from mathEvaluation import MathEvaluation
from Operator import Operator

POST = 1
PRE = -1


class Algorithm:

    def __init__(self, operators: dict):
        self.operators = operators
        self.UNARYS = [op for op in self.operators if not self.operators[op].isBinary]
        self.POSTFIX_UNARYS = [op for op in self.operators if self.operators[op].getPosition() == 1]
        self.PREFIX_UNARYS = [op for op in self.operators if self.operators[op].getPosition() == -1]
        self.MINUS_UNARY = 'N'
        self.operators[self.MINUS_UNARY] = Operator('N', 7, MathEvaluation.neg, False, PRE)

    @staticmethod
    def is_numeric(token):
        try:
            float(token)
            return True
        except ValueError:
            return False

    def is_higher(self, op1, op2):
        if op1 == self.MINUS_UNARY and op2 in ['^', '!', '$', '@', '&']:
            return False
        if self.operators[op1].getKdimut() >= self.operators[op2].getKdimut():
            return True

    def infix_to_postfix(self, expression):
        postfix = []
        stack = []

        for token in expression:
            if Algorithm.is_numeric(token):
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
                while stack and stack[-1] != '(' and self.is_higher(stack[-1], token):
                    postfix.append(stack.pop())
                stack.append(token)

        if '(' in stack or ')' in stack:
            raise ValueError("not matching parentheses")
        while stack:
            postfix.append(stack.pop())

        return postfix

    @staticmethod
    def convert_to_numbers(postfix_expression):
        for i in range(len(postfix_expression)):
            if Algorithm.is_numeric(postfix_expression[i]):
                postfix_expression[i] = float(postfix_expression[i])

    def tokenize_expression(self, expression):
        tokens = []
        current_token = ''

        for i, char in enumerate(expression):
            if char == self.MINUS_UNARY:
                raise ValueError(f"Invalid character: {self.MINUS_UNARY}")
            elif char.isdigit() or (char == '.' and current_token and '.' not in current_token):
                current_token += char
            elif ((char in self.operators or char in ['(', ')']) and
                  char not in self.UNARYS + ['-']):
                if current_token:
                    tokens.append(current_token)
                    current_token = ''
                tokens.append(char)
            elif char == '-':
                if (i == 0 or expression[i - 1] in self.operators and
                        expression[i - 1] not in self.POSTFIX_UNARYS
                        or expression[i - 1] == '('):
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
            elif token == '-' and tokens[i - 1] not in "0123456789)!":
                tokens[i] = self.MINUS_UNARY
        print(tokens)
        return tokens

    def calculate_expression(self, expression: list) -> float:
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
            return result
