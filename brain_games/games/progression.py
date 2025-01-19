from brain_games import utils
from brain_games.games import consts

INSTRUCTION = consts.INSTRUCTION_PROGRESSION


def get_question_answer():
    x = utils.get_random_number(5, 11)
    begin = utils.get_random_number(1, 40)
    step = utils.get_random_number(1, int((100 - begin) / x - 1))
    progression = (list(range(begin, 100, step)[:x]))
    i = utils.get_random_number(0, len(progression) - 1)
    right_answer = str(progression[i])
    progression[i] = '..'
    random_question = ''
    for item in progression:
        random_question = random_question + ' ' + str(item)
    return random_question, right_answer
