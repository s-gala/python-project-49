import math
from random import randint

INSTRUCTION = "Find the greatest common divisor of given numbers." 


def question_answer_gcd():
    x = randint(1, 100)
    y = randint(1, 100)
    random_question = str(x) + ' ' + str(y)
    right_answer = str(math.gcd(x, y))
    return random_question, right_answer
