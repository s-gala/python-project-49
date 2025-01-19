#!/usr/bin/env python3

def main():
    from brain_games.engine import game_engine
    from brain_games.games import gcd

    game_engine(gcd)


if __name__ == '__main__':
    main() 
