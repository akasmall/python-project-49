# file <brain_even.py>

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
        # вычисляем выражение игры
        calculation_result = gl.calculation_result_even(random_number)
        # задаем вопрос юзеру
        gl.question(random_number)
        # получаем ответ и проверяем
        result_user = gl.answer_user('even', random_number)
        # выводим результат игры
        gl.display_game_result(
            name_user,
            calculation_result,
            result_user
            )
    # поздравляем юзера
    print(f"Congratulations, {name_user}!")


"""
if __name__ == '__main__':
    main()
"""
