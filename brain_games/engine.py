from brain_games.scripts.cli import welcome_user, get_answer

MAX_SCORE = 3

def game_run(game):
    player_name = welcome_user(game.RULES)

    score = 0

    while score < MAX_SCORE:

        question, correct = game.run_game()

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