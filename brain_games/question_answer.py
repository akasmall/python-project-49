import prompt
import random
import math


def greeting_user():                            # приветствуем юзера
    print('Welcome to the Brain Games!')


def give_name():                                # узнаем имя
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return name


def task_to_the_user(name_game):                # объясняем задание юзеру
    if name_game == 'even':
        print('Answer "yes" if the number is even, otherwise answer "no".')
    elif name_game == 'calc':
        print('What is the result of the expression?')
    elif name_game == 'gcd':
        print('Find the greatest common divisor of given numbers.')
    else:
        print('Something went wrong. Unknown game!')


def random_sign(sign):                  # получаем случайный знак из списка
    random.shuffle(sign)
    return random.choice(sign)


def random_number(number_1, number_2):          # получаем случайное число
    return random.randint(number_1, number_2)


# задаем вопрос/задачу юзеру
def question(random_number_1, random_number_2='', random_sign=''):
    result = f'{random_number_1} {random_sign} {random_number_2}'
    print(f'Question: {result}')


# проверяем ответ для игры brain_even
def checking_answer_even(value_task, answer_user):
    if answer_user.lower() != 'yes':
        if answer_user.lower() != 'no':
            return False
    if ((value_task % 2 == 0 and answer_user == 'yes') or
            (value_task % 2 != 0 and answer_user == 'no')):
        return True
    else:
        return False


# проверяем ответ для игры brain_calc и brain_gcd
def checking_answer(value_task, answer_user):
    if value_task == answer_user:
        return True
    else:
        return False


# получаем ответ на вопрос от юзера
def answer_user(value_game, value_task):
    result = False
    # получаем ответ юзера
    answer_user = prompt.string('Your answer: ')
    # проверяем результат в зависимости от игры
    if value_game == 'even':
        result = checking_answer_even(value_task, answer_user)
    elif value_game == 'calc' or value_game == 'gcd':
        result = checking_answer(value_task, int(answer_user))
    return result


# вычисляем результат игры brain_calc
def expression_calculation(random_number_1, random_number_2, random_sign):
    result = eval(f'{random_number_1} {random_sign} {random_number_2}')
    return result


# вычисляем результат игры brain_gcd
def calculation_result_gcd(random_number_1, random_number_2):
    result = math.gcd(random_number_1, random_number_2)
    return result
