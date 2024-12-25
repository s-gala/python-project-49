import random
from random import randint

INSTRUCTION = "What is result of the expression?" 


def question_answer_calc():
    x = randint(1, 100)
    y = randint(1, 100)
    math_symbol = ['+', '-', '*']
    random_math_symbol = random.choice(math_symbol)
    random_question = str(x) + random_math_symbol + str(y)
    right_answer = str(eval(random_question))
    return random_question, right_answer
