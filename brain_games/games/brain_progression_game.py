# file <brain_progression_game.py>

from brain_games import game_logic as gl


# def main():
def brain_progression_game():
    # приветствуем игрока
    gl.greeting_user()
    # узнаем имя юзера
    name_user = gl.give_name()
    # объясняем задачу игроку
    gl.task_to_the_user("progression")
    # даем три попытки
    for i in range(0, 3):
        # получаем и случайное число начала прогрессии
        random_number_start = gl.random_number(1, 19)
        # случайное число - шаг прогрессии
        random_number_step = gl.random_number(1, 9)
        # случайное число, которое прячем
        random_number_hide = gl.random_number(1, 9)
        # получаем случайную прогрессию с типом строка
        string_progression = gl.random_progression(
            random_number_start,
            random_number_start + 10 * random_number_step,
            random_number_step
        )
        # print(string_progression)
        hidden_number = string_progression[random_number_hide]
        # прячем чмсло прогрессии и получаем результат для вопроса юзеру
        calculation_result = gl.calculation_result_progression(
            string_progression,
            random_number_hide
        )
        # задаем задачу юзеру вычислить
        gl.question(calculation_result)
        # получаем ответ от юзер
        answer_user_value = gl.answer_user()
        # проверяем ответ от юзер
        result_task = gl.checking_answer(
            hidden_number,
            answer_user_value
            )
        # выводим результат игры
        gl.display_game_result(
            name_user,
            hidden_number,
            answer_user_value,
            result_task
            )
    # поздравляем юзера
    print(f"Congratulations, {name_user}!")
