#!/usr/bin/env python3

def main():
    from brain_games.games import for_all_games, for_brain_progression
    name = for_all_games.welcome_user()
    instruction = for_brain_progression.instruction
    questions_answers_progression = \
        for_brain_progression.question_answer_progression()
    for_all_games.game_engine(instruction, questions_answers_progression, name)


if __name__ == '__main__':
    main() 
