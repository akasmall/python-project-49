"""файл игрового модуля brain_even_game"""
import random

RULES = 'Answer "yes" if the number is even, otherwise answer "no".'
LOWER_BOUND = 1
UPPER_BOUND = 99


def is_number_even(number):
    '''проверка числа на четность'''
    if number % 2 == 0:
        return True
    else:
        return False


def get_question_solution(lower_bound=LOWER_BOUND, upper_bound=UPPER_BOUND):
    '''получаем строку вопроса и результат задачи brain_even'''
    number = random.randint(lower_bound, upper_bound)
    if is_number_even(number):
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return str(number), correct_answer
