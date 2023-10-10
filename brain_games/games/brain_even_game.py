"""file <brain_even_game.py>."""
import random


def question_user():
    """ получаем  случайное число. """
    # получаем и запоминаем два случайных числа
    return str(random.randint(1, 99))


def calculation_result(str_expression):
    """вычисляем результат для игры brain_even."""
    return 'yes' if int(str_expression) % 2 == 0 else 'no'


def even_game():
    """
    зовем общую логику игры на выполнение.
    task_user - задача для юзера
    question_user - текст ждля вопроса
    calculation_result - результат задачи
    """
    task_user = 'Answer "yes" if the number is even, otherwise answer "no".'
    return task_user, question_user, calculation_result


# brain_even_game()
