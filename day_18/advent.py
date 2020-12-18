from itertools import zip_longest


def evaluate(expression):
    terms = expression.split(' ')
    operators = [op for op in terms if not op.isdigit()]
    operands = [int(op) for op in terms if op.isdigit()]
    evaluated_expression = operands[0]

    prev_operator = '+'
    for operand, operator in zip_longest(operands[1:], operators[1:]):
        if (prev_operator == '+'):
            evaluated_expression += operand
        elif (prev_operator == '*'):
            evaluated_expression *= operand
        prev_operator = operator
    return evaluated_expression


with open('input.txt', 'r') as file:
    expressions = file.read().split('\n')
    answer = 0
    for e in expressions:
        print(evaluate(e))
