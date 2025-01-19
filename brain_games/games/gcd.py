import math

from brain_games.games import consts

INSTRUCTION = consts.INSTRUCTION_GCD


def get_question_answer():
    from brain_games import utils
    x = utils.get_random_number(1, 100)
    y = utils.get_random_number(1, 100)
    random_question = f'{x} {y}'
    right_answer = str(math.gcd(x, y))
    return random_question, right_answer
