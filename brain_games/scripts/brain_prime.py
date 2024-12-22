#!/usr/bin/env python3

def main():
    from brain_games.games import for_all_games, for_brain_prime
    name = for_all_games.welcome_user()
    instruction = for_brain_prime.instruction
    questions_answers_prime = for_brain_prime.question_answer_prime()
    for_all_games.game_engine(instruction, questions_answers_prime, name)


if __name__ == '__main__':
    main() 
