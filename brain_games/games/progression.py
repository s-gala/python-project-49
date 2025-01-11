INSTRUCTION = "What number is missing in the progression?"


def question_answer_progression():
    from brain_games.games import random_number
    x = random_number.get_random_number(5, 11)
    begin = random_number.get_random_number(1, 40)
    step = random_number.get_random_number(1, int((100 - begin) / x - 1))
    progression = (list(range(begin, 100, step)[:x]))
    i = random_number.get_random_number(0, len(progression) - 1)
    right_answer = str(progression[i])
    progression[i] = '..'
    random_question = ''
    for item in progression:
        random_question = random_question + ' ' + str(item)
    return random_question, right_answer
