import prompt
from brain_games.scripts.cli import get_answer


MAX_SCORE = 3


def run_game(game):
    print('Welcome to the Brain Games!\n{}\n'.format(game.RULES))
    player_name = prompt.string('May I have your name? ')
    print('Hello, ' + player_name + '!')

    score = 0

    while score < MAX_SCORE:

        question, correct = game.get_challenge()

        answer = get_answer(question)

        if answer != correct:
            print(
                f"'{answer}' is wrong answer ;(.",
                f"Correct answer was '{correct}'.",
            )
            print(f"Let's try again, {player_name}!")
            return
        print("Correct")
        score += 1

    print(f"Congratulations, {player_name}!")