#!/usr/bin/env python3
"""игра brain_prime"""
from brain_games import engine as gl
from brain_games.games import brain_prime_game as b_pri_g


def main():
    """начинаем играть в brain_prime """
    gl.start_game(b_pri_g)


if __name__ == '__main__':
    main()
