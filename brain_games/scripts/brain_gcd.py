#!/usr/bin/env python3

def main():
    from brain_games.games import for_all_games, for_brain_gcd
    name = for_all_games.welcome_user()
    instruction = for_brain_gcd.instruction
    questions_answers_gcd = for_brain_gcd.question_answer_gcd()
    for_all_games.game_engine(instruction, questions_answers_gcd, name)


if __name__ == '__main__':
    main() 
