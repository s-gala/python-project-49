import random
from random import randint

instruction = "What is result of the expression?" 


def question_answer_calc():
    questions_answers_calc = []
    for i in range(1, 4):
        x = randint(1, 100)
        y = randint(1, 100)
        math_symbol = ['+', '-', '*']
        random_math_symbol = random.choice(math_symbol)
        random_question = str(x) + random_math_symbol + str(y)
        right_answer = str(eval(random_question))
        questions_answers_calc.append([random_question, right_answer])
    return questions_answers_calc
