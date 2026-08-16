import random

import prompt

ROUNDS_TO_WIN = 3
MIN_NUMBER = 1
MAX_NUMBER = 100

DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(number):
    return number % 2 == 0


def play():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print(DESCRIPTION)
    for _ in range(ROUNDS_TO_WIN):
        number = random.randint(MIN_NUMBER, MAX_NUMBER)
        correct_answer = 'yes' if is_even(number) else 'no'
        print(f'Question: {number}')
        answer = prompt.string('Your answer: ')
        if answer != correct_answer:
            print(f"'{answer}' is wrong answer ;(. "
                  f"Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            return
        print('Correct!')
    print(f'Congratulations, {name}!')