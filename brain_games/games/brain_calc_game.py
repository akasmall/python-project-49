"""файл игрового модуля brain_calc_game"""
import random

TASK_USER = 'What is the result of the expression?'


def calc_plus(operand_first, operand_second):
    """ вычисляем в игре калькулятор сумму. """
    return operand_first + operand_second


def calc_minus(operand_first, operand_second):
    """ вычисляем в игре калькулятор разницу. """
    return operand_first - operand_second


def calc_multiply(operand_first, operand_second):
    """ вычисляем в игре калькулятор умножение. """
    return operand_first * operand_second


def question_user():
    """ получаем строку вопроса и результат задачи brain_calc """
    # получаем и запоминаем два случайных числа
    random_number_1 = str(random.randint(1, 19))
    random_number_2 = str(random.randint(1, 19))
    # определяем случайный знак
    sign = ['+', '-', '*']
    random_sign = random.choice(sign)
    str_question = f'{random_number_1} {random_sign} {random_number_2}'
    # словарь знаков
    dist_sign = {
        '+': calc_plus,
        '-': calc_minus,
        '*': calc_multiply,
    }
    # ищем, полученный случайный знак в словаре и зовем вычисление
    value_solution_task = dist_sign[random_sign](
        int(random_number_1), int(random_number_2))

    return str_question, value_solution_task
