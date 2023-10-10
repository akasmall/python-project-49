#!/usr/bin/env python3
"""file <brain_even.py>"""
from brain_games import game_logic as gl
from brain_games.games import brain_even_game as b_e_g


def main():
    """игра brain_even.py"""
    tuple_even_game = b_e_g.even_game()
    gl.beginning_game(*tuple_even_game)


if __name__ == '__main__':
    main()
