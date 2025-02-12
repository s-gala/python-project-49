import random

from brain_games.consts import CALC_INSTRUCTION
from brain_games.engine import game_engine
from brain_games.utils import get_random_number


def get_question_answer():
    first_num, second_num = get_random_number(1, 100), get_random_number(1, 100)
    sign, right_answer = get_math_operation(first_num, second_num)
    question = f'{first_num} {sign} {second_num}'
    return question, str(right_answer)


def get_math_operation(first_num, second_num):
    return random.choice([
        ('+', first_num + second_num),
        ('-', first_num - second_num),
        ('*', first_num * second_num)
    ])


def start_calc():
    return game_engine(CALC_INSTRUCTION, get_question_answer)