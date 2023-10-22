#!/usr/bin/env python3
"""игра brain_even"""
from brain_games.engine import launch_game
from brain_games.games import even


def main():
    """начили играть в brain_even """
    launch_game(even)


if __name__ == '__main__':
    main()
