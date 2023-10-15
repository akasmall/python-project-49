#!/usr/bin/env python3
""" file <brain_gcd.py> """
from brain_games import game_logic as gl
from brain_games.games import brain_gcd_game as b_g_g


def main():
    """игра brain_gcd"""
    tuple_gcd_game = b_g_g.gcd_game()
    gl.beginning_game(*tuple_gcd_game)


if __name__ == '__main__':
    main()
