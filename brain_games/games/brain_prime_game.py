"""file <brain_prime_game.py>."""

from brain_games import game_logic as gl


def brain_prime_game():
    """Игра: «Арифметическая прогрессия»"""
    # приветствуем игрока
    gl.greeting_user()
    # узнаем имя юзера
    name_user = gl.give_name()
    # объясняем задачу игроку
    gl.task_to_the_user("prime")
    # даем три попытки
    for _ in range(3):
        # получаем случайное число
        lower_number_sequence = 2
        upper_number_sequence = 99
        number_sequence_prime = gl.random_number(lower_number_sequence,
                                                 upper_number_sequence)
        # задаем задачу игроку
        gl.question(number_sequence_prime)
        # получаем ответ от игрока
        # answer_user_value = gl.answer_user_str()
        answer_user_value = gl.answer_user()
        # вычисляем число введенное игроком - простое?
        calculation_result = gl.calculation_result_prime(lower_number_sequence,
                                                         upper_number_sequence,
                                                         number_sequence_prime)
        # проверяем ответ от игрока
        result_task = gl.checking_answer(calculation_result,
                                         answer_user_value)
        # выводим результат игры
        gl.display_game_result(name_user,
                               calculation_result,
                               answer_user_value,
                               result_task)
    # поздравляем игрока
    print(f"Congratulations, {name_user}!")
