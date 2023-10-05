"""file <brain_prime_game.py>."""
from brain_games import game_logic as gl


def task_user():
    """объясняем задачу игроку"""
    print('Answer "yes" if given number is prime. Otherwise answer "no".')


def question_user():
    """ получаем  случайное число. """
    # # получаем случайное число из диапазона
    number_sequence_prime = gl.random_number(2, 99)
    return str(number_sequence_prime)


def calculation_result(prime_number):
    """вычисляем результат игры brain_calc."""
    # вычисляем введенное игроком число принадлежит простым числам
    prime_number_result = 0
    for number in range(2, int(prime_number)):
        if (int(prime_number) % number) == 0:
            prime_number_result = 1
            break
    return 'yes' if prime_number_result == 0 else 'no'


def brain_prime_game():
    """
    Игра: «Арифметическая прогрессия»
    task_user - задача для юзера
    question_user - текст ждля вопроса
    calculation_result - результат задачи
    """
    gl.beginning_game(task_user, question_user, calculation_result)


# brain_prime_game()
