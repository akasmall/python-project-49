#!/usr/bin/env python3
"""игра brain_gcd"""
from brain_games.engine import launch_game
from brain_games.games import gcd


def main():
    """начинаем играть в brain_gcd """
    launch_game(gcd)


if __name__ == '__main__':
    main()
