"""Логика игр."""
import random
import prompt


def greeting_user():
    """приветствуем юзера."""
    print('Welcome to the Brain Games!')


def give_name():
    """узнаем имя."""
    name_user = prompt.string('May I have your name? ')
    print(f'Hello, {name_user}!')
    return name_user


def random_number(number_1, number_2):
    """получаем случайное число."""
    return random.randint(number_1, number_2)


def question(str_question):
    """задаем вопрос/задачу юзеру."""
    print(f'Question: {str_question}')


def answer_user():
    """получаем ответ от пользователя."""
    return prompt.string('Your answer: ')


def checking_answer(calculation_value, answer_user_value):
    """проверяем результат."""
    return True if str(calculation_value) == str(answer_user_value) else False


def display_game_result(name_user, rigth_value, answer_user_value, task_value):
    """выводим результат игры."""
    if task_value is False:
        # неправильный ответ юзера
        print(f"'{answer_user_value}' is wrong answer ;(. Correct answer was "
              f"'{rigth_value}'.\n"
              f"Let's try again, {name_user}!")
        exit()
    else:
        # правильный ответ юзера
        print('Correct!')


# def beginning_game(task_user, question_user, calculation_result):
# def beginning_game(task_user, question_user):
def beginning_game(game_module):
    """основная функция."""
    greeting_user()
    # узнаем имя
    name_user = give_name()
    # объясняем задачу игроку
    # print(task_user)
    print(game_module.TASK_USER)
    # задаем три задачи
    for _ in range(3):
        # получаем выражение для вопроса
        # value_question_solution = question_user()
        value_question_solution = game_module.question_user()
        # вычисляем выражение игры
        # task_result = calculation_result(question_print)
        # print(f'Вычисленный ответ: {task_result}')
        # задаем вопрос юзеру
        question(value_question_solution[0])
        # получаем ответ от юзера
        answer_user_value = answer_user()
        # print(f'Ответ юзера: {answer_user_value}')
        # проверяем ответ от юзер
        user_result = checking_answer(
            value_question_solution[1], answer_user_value)
        # print(f'Результат юзера: {answer_user_value}')
        # выводим результат игры
        display_game_result(name_user, value_question_solution[1],
                            answer_user_value, user_result)
    # поздравляем юзера
    print(f"Congratulations, {name_user}!")
