# file <brain_gcd.py>

from brain_games import game_logic as gl


def brain_gcd_game():
    # приветствуем игрока
    gl.greeting_user()
    # узнаем имя юзера
    name_user = gl.give_name()
    # объясняем задачу игроку
    gl.task_to_the_user("gcd")
    # даем три попытки
    for i in range(0, 3):
        # получаем и запоминаем два случайных числа
        random_number_1 = gl.random_number(1, 99)
        random_number_2 = gl.random_number(1, 99)
        # вычисляем выражение игры
        calculation_result = gl.calculation_result_gcd(random_number_1,
                                                       random_number_2
                                                       )
        # print(calculation_result)
        # задаем задачу юзеру вычислить
        gl.question(random_number_1, random_number_2)
        # получаем ответ и проверяем
        result_user = gl.answer_user('gcd', calculation_result)
        # выводим результат игры
        gl.display_game_result(
            str(name_user),
            calculation_result,
            bool(result_user)
        )
    # поздравляем юзера
    print(f"Congratulations, {name_user}!")
