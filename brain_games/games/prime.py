"""файл игрового модуля brain_prime_game"""
import random

RULES = 'Answer "yes" if given number is prime. Otherwise answer "no".'
LOWER_BOUND = 2
UPPER_BOUND = 99


def is_number_prime(number, lower_bound):
    """проверка простого числа"""
    if number < lower_bound + 2:
        return True
    sequence_prime_numbers = 0
    for current_number in range(lower_bound, number):
        if number % current_number == 0:
            sequence_prime_numbers = 1
            break
    return sequence_prime_numbers == 0


def get_question_solution(lower_bound=LOWER_BOUND, upper_bound=UPPER_BOUND):
    """получаем случайное число из диапазона и результат задачи brain_prime"""
    number = random.randint(lower_bound, upper_bound)
    if is_number_prime(number, lower_bound):
        correct_answer = 'yes'
    else:
        correct_answer = 'no'

    return str(number), correct_answer
