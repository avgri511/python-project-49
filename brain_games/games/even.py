import random

MIN_NUMBER = 1
MAX_NUMBER = 100

DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(number):
    return number % 2 == 0


def generate_round():
    number = random.randint(MIN_NUMBER, MAX_NUMBER)
    correct_answer = 'yes' if is_even(number) else 'no'
    return number, correct_answer