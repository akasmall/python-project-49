import prompt
import random


def greeting_user():
    print('Welcome to the Brain Games!')


def give_name():
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return name


def task_to_the_user(name_game):
    if name_game == 'even':
        print('Answer "yes" if the number is even, otherwise answer "no".')
    elif name_game == 'calc':
        print('What is the result of the expression?')
    else:
        print('Something went wrong. Unknown game!')


def random_sign(sign):
    random.shuffle(sign)
    return random.choice(sign)


def random_number(number_1, number_2):
    return random.randint(number_1, number_2)


def question(random_number_1, random_number_2='', random_sign=''):
    result = f'{random_number_1} {random_sign} {random_number_2}'
    print(f'Question: {result}')


def checking_answer_even(value_task, answer_user):
    if answer_user.lower() != 'yes':
        if answer_user.lower() != 'no':
            return False
    if ((value_task % 2 == 0 and answer_user == 'yes') or
            (value_task % 2 != 0 and answer_user == 'no')):
        return True
    else:
        return False


def checking_answer_calc(value_task, answer_user):
    if value_task == answer_user:
        return True
    else:
        return False


def answer_user(value_game, value_task):
    result = False
    # получаем ответ юзера
    answer_user = prompt.string('Your answer: ')
    # проверяем результат в зависимости от игры
    if value_game == 'even':
        result = checking_answer_even(value_task, answer_user)
    elif value_game == 'calc':
        result = checking_answer_calc(value_task, int(answer_user))
    return result


def expression_calculation(random_number_1, random_number_2, random_sign):
    res = eval(f'{random_number_1} {random_sign} {random_number_2}')
    return res
