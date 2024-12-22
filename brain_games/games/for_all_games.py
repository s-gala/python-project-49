import prompt


def welcome_user():
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return name


def game_engine(instruction, questions_answers_calc, name):
    print(instruction)
    for item in questions_answers_calc:
        random_question, right_answer = item
        print('Question: ' + str(random_question))
        answer = prompt.string('Your answer: ')
        if right_answer != answer:
            print(f"'{answer}' is wrong answer;(. ", end='')
            print(f"Correct answer was '{right_answer}'.")
            print(f"Let's try again, {name}!")
            break
        else:
            print('Correct!')
    else:
        print(f"Congratulations, {name}!")