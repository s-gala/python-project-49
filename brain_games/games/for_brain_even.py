from random import randint

INSTRUCTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def question_answer_even():
    random_question = randint(1, 100)
    right_answer = ''
    if random_question % 2 == 0:
        right_answer = 'yes'
    else:
        right_answer = 'no'
    return random_question, right_answer
