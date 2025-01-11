INSTRUCTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def question_answer_prime():
    from brain_games.games import random_number
    random_question = random_number.get_random_number(1, 100)
    k = 0
    for i in range(2, random_question // 2 + 1):
        if (random_question % i == 0):
            k = k + 1
    if (k <= 0):
        right_answer = 'yes'
    else:
        right_answer = 'no'
    return random_question, right_answer
