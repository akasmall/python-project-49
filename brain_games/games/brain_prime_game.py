"""файл игрового модуля brain_prime_game"""
import random

TASK_USER = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def question_user():
    """получаем случайное число из диапазона и результат задачи brain_prime"""
    number_sequence_prime = random.randint(2, 99)
    sequence_prime_numbers = 0
    for number in range(2, int(number_sequence_prime)):
        if (int(number_sequence_prime) % number) == 0:
            sequence_prime_numbers = 1
            break

    value_solution_task = 'yes' if sequence_prime_numbers == 0 else 'no'

    return str(number_sequence_prime), value_solution_task
