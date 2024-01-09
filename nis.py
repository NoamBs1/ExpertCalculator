from inputChecks import *
from mathEvaluation import MathEvaluation
from Operator import Operator


class Algorithm:

    def __init__(self, operators: dict):
        self.operators = operators

    @staticmethod
    def is_numeric(token):
        try:
            float(token)
            return True
        except ValueError:
            return False

    def infix_to_postfix(self, expression):
        postfix = []
        stack = []

        for token in expression:
            if token.startswith('-') and Algorithm.is_numeric(token[1:]):
                postfix.append(token)
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
                while (stack and stack[-1] != '(' and
                       self.operators[stack[-1]].getKdimut() >= self.operators[token].getKdimut()):
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
            if char.isdigit() or char == '.':
                current_token += char
            elif ((char in self.operators.keys() or char in ['(', ')']) and
                  char not in [op for op in self.operators if not self.operators[op].isBinary] + ['-']):
                if current_token:
                    tokens.append(current_token)
                    current_token = ''
                tokens.append(char)
            elif char == '-':
                if i == 0 or expression[i - 1] in self.operators.keys() or expression[i - 1] == '(':
                    current_token += char
                else:
                    if current_token:
                        tokens.append(current_token)
                        current_token = ''
                    tokens.append(char)
            elif char in [op for op in self.operators if self.operators[op].getPosition() == 1]:
                if i + 1 < len(expression) and (Algorithm.is_numeric(expression[i + 1]) or expression[i + 1] == '('):
                    raise ValueError(f"{char} should not be followed by a number")
                else:
                    if current_token:
                        tokens.append(current_token)
                        current_token = ''
                    tokens.append(char)
            elif char in [op for op in self.operators if self.operators[op].getPosition() == -1]:
                if i - 1 > -1 and (Algorithm.is_numeric(expression[i - 1]) or expression[i - 1] == ')'):
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
