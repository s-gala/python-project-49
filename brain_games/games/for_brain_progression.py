from random import randint

instruction = "What number is missing in the progression?"


def question_answer_progression():
    questions_answers_progression = []
    for i in range(1, 4):
        x = randint(6, 11)
        begin = randint(1, 40)
        step = randint(1, int((100 - begin) / x - 1))
        progression = (list(range(begin, 100, step)[:x]))
        i = randint(0, len(progression) - 1)
        right_answer = str(progression[i])
        progression[i] = '..'
        question = ''
        for item in progression:
            question = question + ' ' + str(item)
        questions_answers_progression.append([question, right_answer])
    return questions_answers_progression
