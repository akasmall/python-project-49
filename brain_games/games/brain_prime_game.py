"""file <brain_prime_game.py>."""
import random


def question_user():
    """ получаем  случайное число. """
    # # получаем случайное число из диапазона
    number_sequence_prime = random.randint(2, 99)
    return str(number_sequence_prime)


def calculation_result(prime_number):
    """вычисляем результат игры brain_calc."""
    # вычисляем введенное игроком число принадлежит простым числам
    sequence_prime_numbers = 0
    for number in range(2, int(prime_number)):
        if (int(prime_number) % number) == 0:
            sequence_prime_numbers = 1
            break

    return 'yes' if sequence_prime_numbers == 0 else 'no'


def prime_game():
    """
    Игра: «Арифметическая прогрессия»
    task_user - задача для юзера
    question_user - текст ждля вопроса
    calculation_result - результат задачи
    """
    task_user = 'Answer "yes" if given number is prime. Otherwise answer "no".'
    return task_user, question_user, calculation_result


# brain_prime_game()
