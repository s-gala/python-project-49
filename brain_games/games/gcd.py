import math

from brain_games.consts import GCD_INSTRUCTION
from brain_games.engine import game_engine
from brain_games.utils import get_random_number


def get_question_answer():
    first_num, second_num = get_random_number(1, 100), get_random_number(1, 100)
    question = f'{first_num} {second_num}'
    right_answer = math.gcd(first_num, second_num)
    return question, str(right_answer)


def start_gcd():
    return game_engine(GCD_INSTRUCTION, get_question_answer)