import random

from brain_games.consts import CALC_INSTRUCTION
from brain_games.engine import game_engine
from brain_games.utils import get_random_number

INSTRUCTION = CALC_INSTRUCTION


def get_question_answer():
    first_num, second_num = get_random_number(1, 100), get_random_number(1, 100)
    sign, right_answer = get_math_operation(first_num, second_num)
    question = f'{first_num} {sign} {second_num}'
    return question, right_answer


def get_math_operation(first_num, second_num):
    math_operation = [('+', first_num + second_num), 
               ('-', first_num - second_num),
               ('*', first_num * second_num),
    ]
    random_math_operation = random.choice(math_operation)
    return random_math_operation[0], str(random_math_operation[1]) 


def start_calc():
    return game_engine(INSTRUCTION, get_question_answer)