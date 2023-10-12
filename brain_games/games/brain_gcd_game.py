"""file <brain_gcd_game.py>."""
import math
import random
TASK_USER = 'Find the greatest common divisor of given numbers.'


def question_user():
    """ получаем  случайное число. """
    # получаем и запоминаем два случайных числа
    random_number_1 = str(random.randint(2, 99))
    random_number_2 = str(random.randint(2, 99))
    value_question = f'{random_number_1} {random_number_2}'

    list_expression = value_question.split()
    value_number_1 = int(list_expression[0])
    value_number_2 = int(list_expression[1])
    value_solution = math.gcd(value_number_1, value_number_2)

    return (value_question, value_solution)


# def calculation_result(str_expression):
#     """вычисляем результат игры brain_calc."""
#     # получаем и запоминаем два случайных числа
#     random_number_1, random_number_2 = str_expression.split()
#     value_number_1 = int(random_number_1)
#     value_number_2 = int(random_number_2)
#     return math.gcd(value_number_1, value_number_2)


# def gcd_game():
#     """
#     Игра: «Наибольший общий делитель (НОД)»
#     task_user - задача для юзера
#     question_user - текст ждля вопроса
#     calculation_result - результат задачи
#     """
#     task_user = 'Find the greatest common divisor of given numbers.'
#     return task_user, question_user, calculation_result


# brain_gcd_game()
