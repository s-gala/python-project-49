from brain_games.games import consts

INSTRUCTION = consts.INSTRUCTION_PRIME


def get_question_answer():
    from brain_games import utils
    random_question = utils.get_random_number(1, 100)
    k = 0
    for i in range(2, random_question // 2 + 1):
        if (random_question % i == 0):
            k = k + 1
    right_answer = 'yes' if (k <= 0) else 'no'
    return random_question, right_answer
