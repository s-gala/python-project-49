import prompt


def game_engine(game):
    
    name = prompt.string('Welcome to the Brain Games!\nMay I have your name? ')
    print(f'Hello, {name}!')
    print(game.INSTRUCTION)
    for _ in range(3):
        random_question, right_answer = game.get_question_answer()
        print(f"Question: {random_question}")
        answer = prompt.string('Your answer: ')
        if right_answer == answer:
            print('Correct!')
        else:
            print(f"'{answer}' is wrong answer;(. ", end='')
            print(f"Correct answer was '{right_answer}'.")
            print(f"Let's try again, {name}!")
            return
    return print(f"Congratulations, {name}!")
