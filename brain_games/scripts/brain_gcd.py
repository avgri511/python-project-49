from brain_games.engine import run_game
from brain_games.games.gcd import DESCRIPTION, generate_round


def main():
    run_game(DESCRIPTION, generate_round)


if __name__ == '__main__':
    main()