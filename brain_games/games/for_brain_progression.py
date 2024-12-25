from random import randint

INSTRUCTION = "What number is missing in the progression?"


def question_answer_progression():
    x = randint(6, 11)
    begin = randint(1, 40)
    step = randint(1, int((100 - begin) / x - 1))
    progression = (list(range(begin, 100, step)[:x]))
    i = randint(0, len(progression) - 1)
    right_answer = str(progression[i])
    progression[i] = '..'
    random_question = ''
    for item in progression:
        random_question = random_question + ' ' + str(item)
    return random_question, right_answer
