import random

MIN_LENGTH = 5
MAX_LENGTH = 10
MIN_START = 1
MAX_START = 20
MIN_STEP = 1
MAX_STEP = 10

DESCRIPTION = 'What number is missing in the progression?'


def build_progression(start, step, length):
    progression = []
    for index in range(length):
        progression.append(start + index * step)
    return progression


def generate_round():
    length = random.randint(MIN_LENGTH, MAX_LENGTH)
    start = random.randint(MIN_START, MAX_START)
    step = random.randint(MIN_STEP, MAX_STEP)
    progression = build_progression(start, step, length)

    hidden_index = random.randint(0, length - 1)
    correct_answer = str(progression[hidden_index])

    displayed = [str(number) for number in progression]
    displayed[hidden_index] = '..'
    question = ' '.join(displayed)

    return question, correct_answer