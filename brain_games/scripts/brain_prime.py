#!/usr/bin/env python3
"""игра brain_prime"""
from brain_games import game_logic as gl
from brain_games.games import brain_prime_game as b_pri_g


def main():
    """начинаем играть в brain_prime"""
    gl.beginning_game(b_pri_g)


if __name__ == '__main__':
    main()
