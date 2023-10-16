"""файл игрового модуля brain_gcd_game"""
import math
import random

TASK_USER = 'Find the greatest common divisor of given numbers.'
NUMBER_START = 2
NUMBER_END = 99


def get_question_solution():
    """ получаем строку вопроса и результат задачи brain_gcd_game"""
    random_number_1 = random.randint(NUMBER_START, NUMBER_END)
    random_number_2 = random.randint(NUMBER_START, NUMBER_END)
    str_question = f'{random_number_1} {random_number_2}'
    value_solution_task = math.gcd(random_number_1, random_number_2)

    return str_question, value_solution_task
