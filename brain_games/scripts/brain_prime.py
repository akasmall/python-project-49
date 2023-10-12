#!/usr/bin/env python3
"""games file <brain_prime.py>"""
from brain_games import game_logic as gl
from brain_games.games import brain_prime_game as b_pri_g


def main():
    """игра brain_prime"""
    # tuple_prime_game = b_pri_g.prime_game()
    # gl.beginning_game(*tuple_prime_game)
    gl.beginning_game(b_pri_g)


if __name__ == '__main__':
    main()
