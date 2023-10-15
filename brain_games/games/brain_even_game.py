"""файл игрового модуля brain_even_game"""
import random

TASK_USER = 'Answer "yes" if the number is even, otherwise answer "no".'


def question_user():
    '''получаем строку вопроса и результат задачи brain_even.'''
    str_question = random.randint(1, 99)
    value_solution_task = 'yes' if str_question % 2 == 0 else 'no'

    return str(str_question), value_solution_task
