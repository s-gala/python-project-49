from random import randint

instruction = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def question_answer_prime():
    questions_answers_prime = []
    for i in range(1, 4):
        question = randint(1, 1000)
        k = 0
        for i in range(2, question // 2 + 1):
            if (question % i == 0):
                k = k + 1
        if (k <= 0):
            right_answer = 'yes'
        else:
            right_answer = 'no'
        questions_answers_prime.append([question, right_answer])
    return questions_answers_prime
