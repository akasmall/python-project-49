#!/usr/bin/env python3
# file <brain_games.py>

from brain_games import question_answer as qa
from brain_games.games import brain_even as be
from brain_games.games import brain_calc as bc
import prompt


def main():
    list_game = ['1. brain_even', '2. brain_calc']
    qa.greeting_user()
    print('You have to choose the game!')
    for game in list_game:
        print(game)
    game_selection = prompt.string(':> ')
    match game_selection:
        case 'brain_even':
            name_user = qa.give_name()
            be.brain_even_game(name_user)
        case 'brain_calc':
            name_user = qa.give_name()
            bc.brain_calc_game(name_user)
        case _:
            print(f'Sorry, but the game {game_selection} no!')


if __name__ == '__main__':
    main()
