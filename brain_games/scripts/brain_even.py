#!/usr/bin/env python3
"""игра brain_even"""
from brain_games import engine as gl
from brain_games.games import brain_even_game as b_e_g


def main():
    """начили играть в brain_even """
    gl.start_game(b_e_g)


if __name__ == '__main__':
    main()
