import prompt
import random


def greeting_user():
    print('Welcome to the Brain Games!')


def give_name():
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return name


def task_to_the_user():
    print('Answer "yes" if the number is even, otherwise answer "no".')


def question():
    random_number = random.randint(1, 99)
    print(f'Question: {random_number}')

    return random_number


def checking_answer(number_random, answer_user):
    if ((number_random % 2 == 0 and answer_user == 'yes') or
            (number_random % 2 != 0 and answer_user == 'no')):
        return True
    else:
        return False


def answer_user(number_random):
    result_user = prompt.string('Your answer: ')
    if result_user.lower() != 'yes':
        if result_user.lower() != 'no':
            return False
    if checking_answer(number_random, result_user) is True:
        return True
    else:
        return False
