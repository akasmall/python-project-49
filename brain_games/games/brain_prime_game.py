# file <brain_prime_game.py>

from brain_games import game_logic as gl


def brain_prime_game():
    # приветствуем игрока
    gl.greeting_user()
    # узнаем имя юзера
    name_user = gl.give_name()
    # объясняем задачу игроку
    gl.task_to_the_user("prime")
    # даем три попытки
    for i in range(0, 3):
        # получаем случайное число
        number_sequence_prime = gl.random_number(2, 99)
        # задаем задачу юзеру
        gl.question(number_sequence_prime)
        # получаем ответ от юзер
        # answer_user_value = gl.answer_user_str()
        answer_user_value = gl.answer_user()
        # вычисляем число введенное юзером - простое?
        calculation_result = gl.calculation_result_prime(2,
                                                         99,
                                                         number_sequence_prime)
        # проверяем ответ от юзер
        result_task = gl.checking_answer(calculation_result,
                                         answer_user_value)
        # выводим результат игры
        gl.display_game_result(name_user,
                               calculation_result,
                               answer_user_value,
                               result_task)
    # поздравляем юзера
    print(f"Congratulations, {name_user}!")
