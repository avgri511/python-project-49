import random

MIN_NUMBER = 1
MAX_NUMBER = 100

DESCRIPTION = 'Find the greatest common divisor of given numbers.'


def get_gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def generate_round():
    a = random.randint(MIN_NUMBER, MAX_NUMBER)
    b = random.randint(MIN_NUMBER, MAX_NUMBER)
    question = f'{a} {b}'
    correct_answer = str(get_gcd(a, b))
    return question, correct_answer