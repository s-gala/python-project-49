import prompt

NUMBER_OF_ROUNDS = 3


def game_engine(INSTRUCTION, game):
    
    name = prompt.string('Welcome to the Brain Games!\nMay I have your name? ')
    print(f'Hello, {name}!\n{INSTRUCTION}')
    for _ in range(NUMBER_OF_ROUNDS):
        random_question, right_answer = game()
        print(f"Question: {random_question}")
        answer = prompt.string('Your answer: ')
        if right_answer == answer:
            print('Correct!')
        else:
            print(f"'{answer}' is wrong answer;(. ", end='')
            print(f"Correct answer was '{right_answer}'.")
            print(f"Let's try again, {name}!")
            return
    print(f"Congratulations, {name}!")
