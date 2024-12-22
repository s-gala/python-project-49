#!/usr/bin/env python3

def main():
    from brain_games.games import for_all_games
    from brain_games.games import for_brain_calc
    name = for_all_games.welcome_user()
    instruction = for_brain_calc.instruction
    questions_answers_calc = for_brain_calc.question_answer_calc()
    for_all_games.game_engine(instruction, questions_answers_calc, name)


if __name__=='__main__':
   main() 
