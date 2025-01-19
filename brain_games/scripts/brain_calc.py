#!/usr/bin/env python3

def main():
    from brain_games.engine import game_engine
    from brain_games.games import calc
    game_engine(calc) 
      
             
if __name__ == '__main__':
    main() 
