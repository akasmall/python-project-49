"""файл игрового модуля brain_calc_game"""
import random

RULES = 'What is the result of the expression?'
LOWER_BOUND = 1
UPPER_BOUND = 19


def get_addition(operand_first, operand_second):
    """ вычисляем в игре калькулятор сумму. """
    return operand_first + operand_second


def get_subtraction(operand_first, operand_second):
    """ вычисляем в игре калькулятор разницу."""
    return operand_first - operand_second


def get_multiply(operand_first, operand_second):
    """ вычисляем в игре калькулятор умножение. """
    return operand_first * operand_second


def get_question_solution(lower_bound=LOWER_BOUND, upper_bound=UPPER_BOUND):
    """ получаем строку вопроса и результат задачи brain_calc """
    # получаем и запоминаем два случайных числа
    number_1 = str(random.randint(lower_bound, upper_bound))
    number_2 = str(random.randint(lower_bound, upper_bound))
    # определяем случайный знак
    sign = ['+', '-', '*']
    choice_sign = random.choice(sign)
    question = f'{number_1} {choice_sign} {number_2}'
    # словарь знаков
    symbol_function = {
        '+': get_addition,
        '-': get_subtraction,
        '*': get_multiply,
    }
    # ищем, полученный случайный знак в словаре и зовем вычисление
    correct_answer = symbol_function[choice_sign](
        int(number_1), int(number_2))

    return question, str(correct_answer)
