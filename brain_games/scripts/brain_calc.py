#!/usr/bin/env python3
""" игра file <brain_calc.py> """
from brain_games import game_logic as gl
from brain_games.games import brain_calc_game as b_c_g


def main():
    """ игра brain_calc"""
    # tuple_calc_game = b_c_g.calc_game()
    # gl.beginning_game(*tuple_calc_game)
    gl.beginning_game(b_c_g)


if __name__ == '__main__':
    main()
