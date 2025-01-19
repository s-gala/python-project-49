#!/usr/bin/env python3

def main():
    from brain_games.engine import game_engine
    from brain_games.games import progression

    game_engine(progression)


if __name__ == '__main__':
    main() 
