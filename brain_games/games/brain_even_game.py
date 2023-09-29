# file <brain_even_game.py>

from brain_games import game_logic as gl


# def main():
def brain_even_game():
    # приветствуем игрока
    gl.greeting_user()
    # узнаем имя
    name_user = gl.give_name()
    # объясняем задачу игроку
    gl.task_to_the_user("even")
    # даем три попытки
    for i in range(0, 3):
        # запоминаем случайное число
        random_number = gl.random_number(1, 99)
        print(f'Random number: {random_number}')
        # вычисляем выражение игры
        calculation_result = gl.calculation_result_even(random_number)
        print(f'Вычисленный ответ: {calculation_result}')
        # задаем вопрос юзеру
        gl.question(random_number)
        # получаем ответ от юзера тип ЧИСЛО
        # answer_user_value = gl.answer_user_str()
        answer_user_value = gl.answer_user()
        print(f'Ответ юзера: {answer_user_value}')
        # проверяем ответ от юзер
        result_task = gl.checking_answer(calculation_result, answer_user_value)
        # выводим результат игры
        gl.display_game_result(name_user, calculation_result,
                               answer_user_value, result_task)
    # поздравляем юзера
    print(f"Congratulations, {name_user}!")
