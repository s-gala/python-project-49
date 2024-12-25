#!/usr/bin/env python3

def main():
    from brain_games.games import for_all_games, for_brain_prime
    INSTRUCTION = for_brain_prime.INSTRUCTION
    name = for_all_games.welcome_user(INSTRUCTION)
    swapped = True
    i = 1
    while swapped:            
        if i < 4:
            question, answer = for_brain_prime.question_answer_prime()
            swapped = for_all_games.game_engine(question, answer, name)
            i += 1
        else:
            print(f"Congratulations, {name}!")
            break


if __name__ == '__main__':
    main() 