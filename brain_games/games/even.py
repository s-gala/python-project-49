INSTRUCTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def question_answer_even():
    from brain_games.games import random_number
    random_question = random_number.get_random_number(1, 100)
    right_answer = ''
    if random_question % 2 == 0:
        right_answer = 'yes'
    else:
        right_answer = 'no'
    return random_question, right_answer
