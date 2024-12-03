import prompt
from random import randint

name = ''


def welcome_user():
    def name_user():
        global name
        name = prompt.string('May I have your name? ')
    name_user()
    print(f'Hello, {name}!')
    print('Answer "yes" if the number is even, otherwise answer "no".')


def game_even():
    for _ in range(1, 4):
        random_number = randint(1, 100)
        print('Question: ' + str(random_number))
        answer = prompt.string('Your answer: ')
        right_answer = ''
        if random_number % 2 == 0:
            right_answer = 'yes'
        else:
            right_answer = 'no'
        if right_answer != answer:
            print(f"'{answer}' is wrong answer ;(. ", end=' ')
            print(f"Correct answer was '{right_answer}'.")
            print(f'Let\'s try again, {name}!')
            break
        else:
            print('Correct!')
    else:
        print('Congratulations, ' + name + '!')
