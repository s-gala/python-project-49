import prompt

from brain_games.consts import COUNT_OF_ROUNDS

COUNT = COUNT_OF_ROUNDS


def game_engine(INSTRUCTION, game):
    
    name = prompt.string('Welcome to the Brain Games!\nMay I have your name? ')
    print(f'Hello, {name}!\n{INSTRUCTION}')
    for _ in range(COUNT):
        question, right_answer = game()
        print(f"Question: {question}")
        answer = prompt.string('Your answer: ')
        if right_answer == answer:
            print('Correct!')
        else:
            print(f"'{answer}' is wrong answer ;(. \
Correct answer was '{right_answer}'.\nLet's try again, {name}!")
            return
    print(f"Congratulations, {name}!")
