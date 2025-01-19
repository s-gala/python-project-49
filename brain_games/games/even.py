from brain_games.games import consts

INSTRUCTION = consts.INSTRUCTION_EVEN


def get_question_answer():
    from brain_games import utils
    random_question = utils.get_random_number(1, 100)
    right_answer = 'yes' if random_question % 2 == 0 else 'no'
    return random_question, right_answer
