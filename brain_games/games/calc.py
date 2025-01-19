from brain_games import utils
from brain_games.games import consts

INSTRUCTION = consts.INSTRUCTION_CALC


def get_question_answer():
    x, y = utils.get_random_number(1, 100), utils.get_random_number(1, 100)
    sign, operator_metod = utils.get_random_operator()
    random_question = f'{x}{sign}{y}'
    right_answer = str(operator_metod(x, y)) 
    return random_question, right_answer
