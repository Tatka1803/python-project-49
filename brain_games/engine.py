from brain_games.scripts.cli import welcome_user, get_answer

MAX_SCORE = 3


def game_run(game):
    score = 0
    name = welcome_user(game.RULES)
    while score < MAX_SCORE:
        question, correct = game.run_game()
        answer = get_answer(question)
        if answer != correct:
            print(
                f"'{answer}' is wrong answer ;(.",
                f"Correct answer was '{correct}'.",
            )
            print(f"Let's try again, {name}!")
            return
        print("Correct")
        score += 1

    print(f"Congratulations, {name}!")
