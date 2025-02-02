from brain_games import consts
from brain_games.engine import game_engine
from brain_games.utils import get_random_number

INSTRUCTION = consts.INSTRUCTION_EVEN


def get_question_answer():
    random_question = get_random_number(1, 100)
    right_answer = 'yes' if is_even(random_question) else 'no'
    return random_question, right_answer


def is_even(num):
    return num % 2 == 0


def start_even():
    return game_engine(INSTRUCTION, get_question_answer)