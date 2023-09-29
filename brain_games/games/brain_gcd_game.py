# file <brain_gcd_game.py>

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
        # print(random_number_1)
        random_number_2 = gl.random_number(1, 99)
        # print(random_number_2)
        # вычисляем выражение игры
        calculation_result = gl.calculation_result_gcd(random_number_1,
                                                       random_number_2)
        # print(f'Правильный ответ: {calculation_result}')
        # задаем задачу юзеру вычислить
        gl.question(random_number_1, random_number_2)
        # получаем ответ от юзера вводом ЧИСЛА
        # answer_user_value = gl.answer_user_int()
        answer_user_value = gl.answer_user()
        # print(f'Ответ юзера: {answer_user_value}')
        # проверяем ответ от юзер
        result_task = gl.checking_answer(calculation_result, answer_user_value)
        # print(f'Проверка ответа {result_task}')
        # выводим результат игры
        gl.display_game_result(
            name_user,
            calculation_result,
            answer_user_value,
            result_task)    # поздравляем юзера
    print(f"Congratulations, {name_user}!")


# brain_gcd_game()
