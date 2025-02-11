from brain_games.consts import PROGRESSION_INSTRUCTION
from brain_games.engine import game_engine
from brain_games.utils import get_random_number

INSTRUCTION = PROGRESSION_INSTRUCTION


def get_question_answer():
    progression = [num for num in range(get_random_number(1, 40), 130, get_random_number(1, 11))][:get_random_number(5,11)] 
    index_hidden_num = get_random_number(0, len(progression) - 1)
    right_answer = progression[index_hidden_num]
    progression[index_hidden_num] = '..'
    return ' '.join(str(num) for num in progression), str(right_answer)


def start_progression():
    return game_engine(INSTRUCTION, get_question_answer)