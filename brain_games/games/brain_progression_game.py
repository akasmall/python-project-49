"""file <brain_progression_game.py>."""
import random
TASK_USER = 'What number is missing in the progression?'


def calculation_result_progression(string_progression, random_hide_number):
    """вычисляем результат игры brain_progression."""
    result = string_progression
    result[random_hide_number] = '..'
    return result


def question_user():
    """ получаем  случайное число. """
    # получаем и случайное число начала прогрессии
    random_number_start = random.randint(1, 19)
    # случайное число - шаг прогрессии
    random_number_step = random.randint(1, 9)
    # случайное число по порядку из длины прогрессии, которое спрячем
    random_number_hide = random.randint(2, 8)
    # получаем случайную прогрессию со случайным шагом.
    random_number_finish = random_number_start + 10 * random_number_step
    # случайное число по порядку из длины прогрессии, которое спрячем
    progression = range(random_number_start,
                        random_number_finish,
                        random_number_step)
    string_progression_question = list(map(str, progression))
    # # прячем число прогрессии и получаем результат для вопроса игроку
    value_question = calculation_result_progression(
        string_progression_question,
        random_number_hide)

    value_question = f'{" ".join(value_question)}'

    list_expression = value_question.split()
    hidden_number = list_expression.index('..')
    if hidden_number < 8:
        index_plus_2 = int(list_expression[hidden_number + 2])
        index_plus_1 = int(list_expression[hidden_number + 1])
        result_number_upper = index_plus_2 - index_plus_1
        value_solution = index_plus_1 - result_number_upper
    else:
        index_plus_1 = int(list_expression[hidden_number - 1])
        index_plus_2 = int(list_expression[hidden_number - 2])
        result_number_lower = index_plus_1 - index_plus_2
        value_solution = index_plus_1 + result_number_lower
    # return str(task_result)

    return (value_question, value_solution)


def calculation_result(str_expression):
    """вычисляем результат игры brain_calc."""
    # получаем и случайное число начала прогрессии
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


# def progression_game():
#     """
#     Игра: «Простое ли число?».
#     task_user - задача для юзера
#     question_user - текст ждля вопроса
#     calculation_result - результат задачи
#     """
#     task_user = 'What number is missing in the progression?'
#     return task_user, question_user, calculation_result

# brain_progression_game()
