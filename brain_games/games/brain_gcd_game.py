"""файл игрового модуля brain_gcd_game"""
import math
import random

TASK_USER = 'Find the greatest common divisor of given numbers.'


def question_user():
    """ получаем строку вопроса и результат задачи brain_gcd_game. """
    random_number_1 = random.randint(2, 99)
    random_number_2 = random.randint(2, 99)
    str_question = f'{random_number_1} {random_number_2}'
    value_solution_task = math.gcd(random_number_1, random_number_2)

    return str(str_question), value_solution_task
