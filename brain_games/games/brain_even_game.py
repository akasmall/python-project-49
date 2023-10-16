"""файл игрового модуля brain_even_game"""
import random

TASK_USER = 'Answer "yes" if the number is even, otherwise answer "no".'
NUMBER_START = 1
NUMBER_END = 99


def check_even_number(number):
    '''проверка числа на четность'''
    if number % 2 == 0:
        return True
    else:
        return False


def get_question_solution():
    '''получаем строку вопроса и результат задачи brain_even'''
    number = random.randint(NUMBER_START, NUMBER_END)
    if check_even_number(number) is True:
        value_solution_task = 'yes'
    else:
        value_solution_task = 'no'
    return str(number), value_solution_task
