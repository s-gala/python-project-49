import math

from brain_games import consts
from brain_games.engine import game_engine
from brain_games.utils import get_random_number

INSTRUCTION = consts.INSTRUCTION_GCD


def get_question_answer():
    first_num, second_num = get_random_number(1, 100), get_random_number(1, 100)
    random_question = f'{first_num} {second_num}'
    right_answer = str(math.gcd(first_num, second_num))
    return random_question, right_answer


def start_gcd():
    return game_engine(INSTRUCTION, get_question_answer)