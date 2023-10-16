#!/usr/bin/env python3
""" игра brain_calc """
from brain_games import game_logic as gl
from brain_games.games import brain_calc_game as b_c_g


def main():
    """начинаем играть в brain_calc """
    gl.started_finished(b_c_g)


if __name__ == '__main__':
    main()
