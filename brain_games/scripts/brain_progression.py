#!/usr/bin/env python3
"""file <brain_progression.py>"""
from brain_games import game_logic as gl
from brain_games.games import brain_progression_game as b_pro_g


def main():
    """игра brain_progression"""
    # tuple_progression_game = b_pro_g.progression_game()
    # gl.beginning_game(*tuple_progression_game)
    gl.beginning_game(b_pro_g)


if __name__ == '__main__':
    main()
