import math
from random import randint

instruction = "Find the greatest common divisor of given numbers." 


def question_answer_gcd():
    questions_answers_gcd = []
    for i in range(1, 4):
        x = randint(1, 100)
        y = randint(1, 100)
        random_question = str(x) + ' ' + str(y)
        right_answer = str(math.gcd(x, y))
        questions_answers_gcd.append([random_question, right_answer])
    return questions_answers_gcd
