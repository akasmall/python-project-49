"""файл игрового модуля brain_progression_game."""
import random

TASK_USER = 'What number is missing in the progression?'


def calculation_result(str_expression):
    """вычисляем результат игры brain_calc."""
    list_progression = str_expression.split()
    hidden_number = list_progression.index('..')
    if hidden_number < 8:
        index_plus_2 = int(list_progression[hidden_number + 2])
        index_plus_1 = int(list_progression[hidden_number + 1])
        result_number_upper = index_plus_2 - index_plus_1
        task_result = index_plus_1 - result_number_upper
    else:
        index_plus_1 = int(list_progression[hidden_number - 1])
        index_plus_2 = int(list_progression[hidden_number - 2])
        result_number_lower = index_plus_1 - index_plus_2
        task_result = index_plus_1 + result_number_lower
    return str(task_result)


def question_user():
    """ получаем строку вопроса и результат задачи brain_progression"""
    len_sequence = 10
    # получаем случайное число начала прогрессии
    random_number_start = random.randint(1, 19)
    # случайное число - шаг прогрессии
    random_number_step = random.randint(1, 9)
    # случайное число по порядку из длины прогрессии, которое спрячем
    random_number_hide = random.randint(2, 8)
    # получаем случайное число конца прогрессии
    random_number_finish = random_number_start + \
        len_sequence * random_number_step
    # получаем прогрессию
    progression = range(random_number_start,
                        random_number_finish, random_number_step)
    string_progression = list(map(str, progression))
    # # прячем число прогрессии
    string_progression[random_number_hide] = '..'
    str_question = f'{" ".join(string_progression)}'
    # получаем результат для вопроса игроку
    value_solution_task = calculation_result(str_question)

    return str_question, value_solution_task
