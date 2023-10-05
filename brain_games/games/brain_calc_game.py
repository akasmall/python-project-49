"""file <brain_calc_game.py>"""
from brain_games import game_logic as gl


def task_user():
    """объясняем задачу игроку"""
    print('What is the result of the expression?')


def question_user():
    """ получаем  случайное число. """
    # получаем и запоминаем два случайных числа
    random_number_1 = str(gl.random.randint(1, 19))
    random_number_2 = str(gl.random.randint(1, 19))
    # определяем случайный знак
    sign = ['+', '-', '*']
    random_sign = gl.random.choice(sign)
    result = f'{random_number_1} {random_sign} {random_number_2}'
    return result


def calc_plus(operand_first, operand_second):
    """ вычисляем в игре калькулятор сумму. """
    return operand_first + operand_second


def calc_minus(operand_first, operand_second):
    """ вычисляем в игре калькулятор разницу. """
    return operand_first - operand_second


def calc_multiply(operand_first, operand_second):
    """ вычисляем в игре калькулятор умножение. """
    return operand_first * operand_second


def calculation_result(str_expression):
    """вычисляем результат игры brain_calc."""
    # получаем и запоминаем два случайных числа
    random_number_1, value_sign, random_number_2 = str_expression.split()
    value_number_1 = int(random_number_1)
    value_number_2 = int(random_number_2)
    # словарь знаков
    dist_sign = {
        '+': calc_plus,
        '-': calc_minus,
        '*': calc_multiply,
    }
    # ищем, есть ли полученный случайный знак в словаре
    if dist_sign.get(value_sign, False) is not False:
        value_random_sign = dist_sign[value_sign](
            value_number_1, value_number_2)
        return value_random_sign
    else:
        print('Something went wrong!')
        exit()


def brain_calc_game():
    """
    Игра: «Калькулятор»
    task_user - задача для юзера
    question_user - текст ждля вопроса
    calculation_result - результат задачи
    """
    gl.beginning_game(task_user, question_user, calculation_result)


# brain_calc_game()
