"""Логика игр."""
import random
import prompt


def greeting_user():
    """приветствуем юзера."""
    print('Welcome to the Brain Games!')


def give_name():
    """узнаем имя."""
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return name


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


def calculation_result_prime(sequence_prime_numbers, number_sequence_prime):
    """
    получаем последовательность простых чисел для brain_prime и
    проверяем ответ юзера.
    """
    return 'yes' if number_sequence_prime in sequence_prime_numbers else 'no'


# def calculation_result_gcd(random_number_1, random_number_2):
#     """вычисляем результат игры brain_gcd."""
#     return math.gcd(random_number_1, random_number_2)


def calculation_result_progression(string_progression, random_hide_number):
    """вычисляем результат игры brain_progression."""
    result = string_progression
    result[random_hide_number] = '..'
    return result


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


# def start_game(game, task_user, calculation_result):
def beginning_game(task_user, question_user, calculation_result):
    """основная функция."""
    greeting_user()
    # узнаем имя
    name_user = give_name()
    # объясняем задачу игроку
    task_user()
    # задаем три задачи
    for _ in range(3):
        # получаем выражение для вопроса
        question_print = question_user()
        # print(f'Случайное число: {question_print}')
        # вычисляем выражение игры
        task_result = calculation_result(question_print)
        # print(f'Вычисленный ответ: {task_result}')
        # задаем вопрос юзеру
        question(question_print)
        # получаем ответ от юзера тип ЧИСЛО
        answer_user_value = answer_user()
        # print(f'Ответ юзера: {answer_user_value}')
        # проверяем ответ от юзер
        user_result = checking_answer(task_result, answer_user_value)
        # print(f'Результат юзера: {answer_user_value}')
        # выводим результат игры
        display_game_result(name_user, task_result,
                            answer_user_value, user_result)
    # поздравляем юзера
    print(f"Congratulations, {name_user}!")
