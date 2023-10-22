#!/usr/bin/env python3
"""игра brain_prime"""
from brain_games.engine import launch_game
from brain_games.games import prime


def main():
    """начинаем играть в brain_prime """
    launch_game(prime)


if __name__ == '__main__':
    main()
