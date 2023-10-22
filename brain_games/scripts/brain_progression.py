#!/usr/bin/env python3
"""игра brain_progression"""
from brain_games.engine import launch_game
from brain_games.games import progression


def main():
    """начинаем играть в brain_progression """
    launch_game(progression)


if __name__ == '__main__':
    main()
