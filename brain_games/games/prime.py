from brain_games.consts import PRIME_INSTRUCTION
from brain_games.engine import game_engine
from brain_games.utils import get_random_number


def get_question_answer():
    question = get_random_number(1, 100)
    right_answer = 'yes' if get_check_prime(question) else 'no'
    return question, right_answer

    
def get_check_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** (0.5) + 1)):
        if (num % i == 0):
            return False
    return True


def start_prime():
    return game_engine(PRIME_INSTRUCTION, get_question_answer)