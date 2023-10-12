"""file <brain_calc_game.py>"""
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
    """ получаем  случайное число. """
    # получаем и возвращаем два значения: для вопроса и проверки ответа
    random_number_1 = str(random.randint(1, 19))
    random_number_2 = str(random.randint(1, 19))
    # определяем случайный знак
    sign = ['+', '-', '*']
    random_sign = random.choice(sign)
    value_question = (
        f'{random_number_1} {random_sign} ' f'{random_number_2}')
    # return value_question_solution, random_sign

    # random_number_1, value_sign, random_number_2
    list_expression = value_question.split()
    value_number_1 = int(list_expression[0])
    value_number_2 = int(list_expression[2])
    # словарь знаков
    dist_sign = {
        '+': calc_plus,
        '-': calc_minus,
        '*': calc_multiply,
    }
    # ищем, есть ли полученный случайный знак в словаре
    if dist_sign.get(list_expression[1], False) is not False:
        value_random_sign = dist_sign[list_expression[1]](
            value_number_1, value_number_2)
        value_solution = value_random_sign
    else:
        print('Something went wrong!')
        exit()

    return (value_question, value_solution)


# def calculation_value_question_solution(str_expression):
#     """вычисляем результат игры brain_calc."""
#     # получаем и запоминаем два случайных числа
#     random_number_1, value_sign, random_number_2 = str_expression.split()
#     value_number_1 = int(random_number_1)
#     value_number_2 = int(random_number_2)
#     # словарь знаков
#     dist_sign = {
#         '+': calc_plus,
#         '-': calc_minus,
#         '*': calc_multiply,
#     }
#     # ищем, есть ли полученный случайный знак в словаре
#     if dist_sign.get(value_sign, False) is not False:
#         value_random_sign = dist_sign[value_sign](
#             value_number_1, value_number_2)
#         return value_random_sign
#     else:
#         print('Something went wrong!')
#         exit()


# def calc_game():
#     """
#     Игра: «Калькулятор»
#     task_user - задача для юзера
#     question_user - текст ждля вопроса
#     calculation_value_question_solution - результат задачи
#     """
#     task_user = 'What is the value_question_solution of the expression?'
#     # return task_user, question_user, calculation_value_question_solution
#     return task_user, question_user


# brain_calc_game()
