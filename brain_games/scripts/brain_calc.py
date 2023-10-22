#!/usr/bin/env python3
""" игра brain_calc """
from brain_games.engine import launch_game
from brain_games.games import calc


def main():
    """начинаем играть в brain_calc """
    launch_game(calc)


if __name__ == '__main__':
    main()
