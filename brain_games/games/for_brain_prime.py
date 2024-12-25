from random import randint

INSTRUCTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def question_answer_prime():
    random_question = randint(1, 1000)
    k = 0
    for i in range(2, random_question // 2 + 1):
        if (random_question % i == 0):
            k = k + 1
    if (k <= 0):
        right_answer = 'yes'
    else:
        right_answer = 'no'
    return random_question, right_answer
