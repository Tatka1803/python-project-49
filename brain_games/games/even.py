from random import randint

RULES = 'Answer "yes" if number even otherwise answer "no".'


def get_challenge():
    question = randint(1, 100)

    if question % 2 == 0:
        is_even = "yes"
    else:
        is_even = "no"

    return (question, is_even)
