"""файл игрового модуля brain_prime_game"""
import random

TASK_USER = 'Answer "yes" if given number is prime. Otherwise answer "no".'
NUMBER_START = 2
NUMBER_END = 99


def check_prime_number(number_check):
    """проверка простого числа"""
    if number_check == NUMBER_START:
        return False
    sequence_prime_numbers = 0
    for number in range(NUMBER_START, number_check):
        if number_check % number == 0:
            sequence_prime_numbers = 1
            break
    if sequence_prime_numbers == 0:
        return True
    else:
        return False


def get_question_solution():
    """получаем случайное число из диапазона и результат задачи brain_prime"""
    number = random.randint(NUMBER_START, NUMBER_END)
    if check_prime_number(number) is True:
        value_solution_task = 'yes'
    else:
        value_solution_task = 'no'

    return str(number), value_solution_task
