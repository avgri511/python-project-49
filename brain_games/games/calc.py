import random

MIN_NUMBER = 1
MAX_NUMBER = 100
OPERATIONS = ('+', '-', '*')

DESCRIPTION = 'What is the result of the expression?'


def calculate(a, b, operator):
    match operator:
        case '+':
            return a + b
        case '-':
            return a - b
        case '*':
            return a * b


def generate_round():
    a = random.randint(MIN_NUMBER, MAX_NUMBER)
    b = random.randint(MIN_NUMBER, MAX_NUMBER)
    operator = random.choice(OPERATIONS)
    question = f'{a} {operator} {b}'
    correct_answer = str(calculate(a, b, operator))
    return question, correct_answer
