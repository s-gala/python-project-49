import prompt


def welcome_user(INSTRUCTION):
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print(INSTRUCTION)
    return name


def game_engine(random_question, right_answer, name):
    print('Question: ' + str(random_question))
    answer = prompt.string('Your answer: ')
    if right_answer != answer:
        print(f"'{answer}' is wrong answer;(. ", end='')
        print(f"Correct answer was '{right_answer}'.")
        print(f"Let's try again, {name}!")
        return False
    else:
        print('Correct!')
        return True
    