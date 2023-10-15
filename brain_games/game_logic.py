"""общий модуль логики игр"""
import prompt


def print_result_task(name_user, value_solution_task,
                      answer_user_value, result_task):
    """выводим результат игры"""
    if result_task is False:
        # неправильный ответ юзера
        print(f"'{answer_user_value}' is wrong answer ;(. "
              f"Correct answer was "
              f"'{value_solution_task}'.\n"
              f"Let's try again, {name_user}!")
        exit()
    else:
        print('Correct!')


def beginning_game(game_module):
    """начало модуля логики"""
    # greeting_user()
    print('Welcome to the Brain Games!')
    # узнаем имя
    name_user = prompt.string('May I have your name? ')
    print(f'Hello, {name_user}!')
    # объясняем задачу игроку
    print(game_module.TASK_USER)
    # задаем три задачи
    for _ in range(3):
        # получаем значение для вопроса и вычисляем правильнй результат игры
        value_question, value_solution_task = game_module.question_user()
        # print(f'Вычисленный ответ: {value_solution_task}')
        # задаем вопрос юзеру
        print(f'Question: {value_question}')
        # получаем ответ от юзера
        answer_user_value = prompt.string('Your answer: ')
        # проверяем ответ от юзер
        result_task = True if str(value_solution_task) == str(
            answer_user_value) else False
        print_result_task(name_user, value_solution_task,
                          answer_user_value, result_task)
        # if result is False:
        #     # неправильный ответ юзера
        #     print(f"'{answer_user_value}' is wrong answer ;(. "
        #           f"Correct answer was "
        #           f"'{value_solution_task}'.\n"
        #           f"Let's try again, {name_user}!")
        #     exit()
        # else:
        #     print('Correct!')
    print(f"Congratulations, {name_user}!")
