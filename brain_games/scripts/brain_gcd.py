#!/usr/bin/env python3
"""игра brain_gcd"""
from brain_games import game_logic as gl
from brain_games.games import brain_gcd_game as b_g_g


def main():
    """начинаем играть в brain_gcd"""
    gl.beginning_game(b_g_g)


if __name__ == '__main__':
    main()
