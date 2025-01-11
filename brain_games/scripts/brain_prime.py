#!/usr/bin/env python3

def main():
    from brain_games.games import engine, prime
    INSTRUCTION = prime.INSTRUCTION
    name = engine.welcome_user(INSTRUCTION)
    swapped = True
    i = 1
    while swapped:            
        if i < 4:
            question, answer = prime.question_answer_prime()
            swapped = engine.game_engine(question, answer, name)
            i += 1
        else:
            print(f"Congratulations, {name}!")
            break


if __name__ == '__main__':
    main() 
