"""file <brain_progression_game.py>."""

from brain_games import game_logic as gl


def task_user():
    """объясняем задачу игроку"""
    print('What number is missing in the progression?')


def question_user():
    """ получаем  случайное число. """
    # получаем и случайное число начала прогрессии
    random_number_start = gl.random.randint(1, 19)
    # случайное число - шаг прогрессии
    random_number_step = gl.random.randint(1, 9)
    # случайное число по порядку из длины прогрессии, которое спрячем
    random_number_hide = gl.random.randint(2, 8)
    # получаем случайную прогрессию со случайным шагом.
    random_number_finish = random_number_start + 10 * random_number_step
    # случайное число по порядку из длины прогрессии, которое спрячем
    progression = range(random_number_start,
                        random_number_finish,
                        random_number_step)
    string_progression_question = list(map(str, progression))
    # # прячем число прогрессии и получаем результат для вопроса игроку
    result = gl.calculation_result_progression(
        string_progression_question,
        random_number_hide)

    result = f'{" ".join(result)}'
    return result


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


# def main():
def brain_progression_game():
    """
    Игра: «Простое ли число?».
    task_user - задача для юзера
    question_user - текст ждля вопроса
    calculation_result - результат задачи
    """
    gl.beginning_game(task_user, question_user, calculation_result)


# brain_progression_game()
