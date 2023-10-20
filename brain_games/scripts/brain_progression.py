#!/usr/bin/env python3
"""игра brain_progression"""
from brain_games import engine as gl
from brain_games.games import brain_progression_game as b_pro_g


def main():
    """начинаем играть в brain_progression """
    gl.start_game(b_pro_g)


if __name__ == '__main__':
    main()
