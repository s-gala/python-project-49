import random

from brain_games import consts
from brain_games.engine import game_engine
from brain_games.utils import get_random_number

INSTRUCTION = consts.INSTRUCTION_CALC


def get_question_answer():
    first_num, second_num = get_random_number(1, 100), get_random_number(1, 100)
    math_operation = [('+', first_num + second_num), 
                   ('-', first_num - second_num),
                   ('*', first_num * second_num),
    ]
    random_math_operation = random.choice(math_operation)
    random_question = f'{first_num} {random_math_operation[0]} {second_num}'
    right_answer = str(random_math_operation[1]) 
    return random_question, right_answer


def start_calc():
    return game_engine(INSTRUCTION, get_question_answer)