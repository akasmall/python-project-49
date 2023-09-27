# file <brain_calc.py>

from brain_games import game_logic as gl


# def main():
def brain_calc_game():
    # приветствуем игрока
    gl.greeting_user()
    # узнаем имя юзера
    name_user = gl.give_name()
    # объясняем задачу игроку
    gl.task_to_the_user("calc")
    # даем три попытки
    for i in range(0, 3):
        # определяем случайный знак
        random_sign = gl.random_sign(['+', '-', '*'])
        # получаем и запоминаем два случайных числа
        random_number_1 = gl.random_number(1, 9)
        random_number_2 = gl.random_number(1, 9)
        # вычисляем выражение игры
        calculation_result = gl.expression_calculation(random_number_1,
                                                       random_number_2,
                                                       random_sign
                                                       )
        # задаем задачу юзеру вычислить
        gl.question(random_number_1, random_number_2, random_sign)
        # получаем ответ и проверяем
        result_user = gl.answer_user('calc', calculation_result)
        # выводим результат игры
        gl.display_game_result(
            str(name_user),
            calculation_result,
            bool(result_user)
            )
    # поздравляем юзера
    print(f"Congratulations, {name_user}!")


"""
if __name__ == '__main__':
    main()
"""
