import prompt

ROUNDS_TO_WIN = 3


def welcome_user():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return name


def run_game(description, generate_round):
    name = welcome_user()
    print(description)
    for _ in range(ROUNDS_TO_WIN):
        question, correct_answer = generate_round()
        print(f'Question: {question}')
        answer = prompt.string('Your answer: ')
        if answer != correct_answer:
            print(f"'{answer}' is wrong answer ;(. "
                  f"Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            return
        print('Correct!')
    print(f'Congratulations, {name}!')