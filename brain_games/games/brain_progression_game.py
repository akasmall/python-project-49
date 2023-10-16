"""файл игрового модуля brain_progression_game"""
import random

TASK_USER = 'What number is missing in the progression?'
LEN_SEQUENCE = 10
NUMBER_START = 1
NUMBER_END = 19
NUMBER_STEP_START = 1
NUMBER_STEP_END = 9
NUMBER_HIDE_START = 2
NUMBER_HIDE_END = 8


def get_progression():
    """получить прогрессию"""
    len_sequence = LEN_SEQUENCE
    random_number_start = random.randint(NUMBER_START, NUMBER_END)
    random_number_step = random.randint(NUMBER_STEP_START, NUMBER_STEP_END)
    random_number_finish = random_number_start +\
        len_sequence * random_number_step
    progression = range(random_number_start,
                        random_number_finish, random_number_step)
    return progression


def get_str_progression(progression):
    """получаем строку прогрессии и прячем число"""
    str_progression = list(map(str, progression))
    random_number_hide = random.randint(NUMBER_HIDE_START, NUMBER_HIDE_END)
    # # прячем число прогрессии
    str_progression[random_number_hide] = '..'
    return f'{" ".join(str_progression)}'


def calculation_result(str_progression):
    """вычисляем результат игры brain_calc."""
    list_progression = str_progression.split()
    hidden_number = list_progression.index('..')
    number_step_check = NUMBER_STEP_END
    if hidden_number < number_step_check-1:
        index_plus_2 = int(list_progression[hidden_number + 2])
        index_plus_1 = int(list_progression[hidden_number + 1])
        result_number_upper = index_plus_2 - index_plus_1
        task_result = index_plus_1 - result_number_upper
    else:
        index_plus_1 = int(list_progression[hidden_number - 1])
        index_plus_2 = int(list_progression[hidden_number - 2])
        result_number_lower = index_plus_1 - index_plus_2
        task_result = index_plus_1 + result_number_lower
    return task_result


def get_question_solution():
    """ получаем строку вопроса и результат задачи brain_progression"""
    progression = get_progression()
    str_progression = get_str_progression(progression)
    value_solution_task = str(calculation_result(str_progression))

    return str_progression, value_solution_task
