from brain_games.consts import EVEN_INSTRUCTION
from brain_games.engine import game_engine
from brain_games.utils import get_random_number


def get_question_answer():
    question = get_random_number(1, 100)
    right_answer = 'yes' if get_check_even(question) else 'no'
    return question, right_answer


def get_check_even(num):
    return num % 2 == 0


def start_even():
    return game_engine(EVEN_INSTRUCTION, get_question_answer)