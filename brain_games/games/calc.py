import operator
import random

INSTRUCTION = "What is result of the expression?" 


def question_answer_calc():
    from brain_games.games import random_number
    x = random_number.get_random_number(1, 100)
    y = random_number.get_random_number(1, 100)
    math_symbol = {'+': operator.add,
                   '-': operator.sub,
                   '*': operator.mul}
    op = random.choice(list(math_symbol.keys()))
    random_question = f'{x}{op}{y}'
    right_answer = str(math_symbol.get(op)(x, y)) 
    return random_question, right_answer
