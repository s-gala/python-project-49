import math

INSTRUCTION = "Find the greatest common divisor of given numbers." 


def question_answer_gcd():
    from brain_games.games import random_number
    x = random_number.get_random_number(1, 100)
    y = random_number.get_random_number(1, 100)
    random_question = f'{x} {y}'
    right_answer = str(math.gcd(x, y))
    return random_question, right_answer
