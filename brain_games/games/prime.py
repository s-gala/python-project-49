from brain_games import consts
from brain_games.engine import game_engine
from brain_games.utils import get_random_number

INSTRUCTION = consts.INSTRUCTION_PRIME


def get_question_answer():
    random_question = get_random_number(1, 100)
    right_answer = 'yes' if is_prime(random_question) else 'no'
    return random_question, right_answer

    
def is_prime(num):
    acc = 0
    for i in range(2, int(num ** (0.5))):
        if (num % i == 0):
            acc = acc + 1
    return acc == 0


def start_prime():
    return game_engine(INSTRUCTION, get_question_answer)