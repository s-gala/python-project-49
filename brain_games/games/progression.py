from brain_games import consts
from brain_games.engine import game_engine
from brain_games.utils import get_random_number

INSTRUCTION = consts.INSTRUCTION_PROGRESSION


def get_question_answer():
    length_progression = get_random_number(5, 11)
    begin = get_random_number(1, 40)
    step = get_random_number(1, int((100 - begin) / length_progression - 1))
    progression = (list(range(begin, 100, step)[:length_progression]))
    index_hidden_num = get_random_number(0, len(progression) - 1)
    right_answer = str(progression[index_hidden_num])
    progression[index_hidden_num] = '..'
    random_question = (' '.join(str(num) for num in progression))
    return random_question, right_answer


def start_progression():
    return game_engine(INSTRUCTION, get_question_answer)