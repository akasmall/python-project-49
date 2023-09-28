import prompt
import random
import math


# приветствуем юзера
def greeting_user():
    print('Welcome to the Brain Games!')


# узнаем имя
def give_name():
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return name


# объясняем задание юзеру
def task_to_the_user(name_game):
    if name_game == 'even':
        print('Answer "yes" if the number is even, otherwise answer "no".')
    elif name_game == 'calc':
        print('What is the result of the expression?')
    elif name_game == 'gcd':
        print('Find the greatest common divisor of given numbers.')
    elif name_game == 'progression':
        print('What number is missing in the progression?')
    elif name_game == 'prime':
        print('Answer "yes" if given number is prime. Otherwise answer "no".')
    else:
        print('Something went wrong. Unknown game!')


# получаем случайный знак из списка
# а также получаем случайное число для prime
def random_sign(sign):
    random.shuffle(sign)
    return random.choice(sign)


# получаем случайное число
def random_number(number_1, number_2):
    return random.randint(number_1, number_2)


# получаем случайную прогрессию со случайным шагом
def random_progression(number_start, number_finish, step):
    # получаем ссылку на генератор от до и шагом
    progression = range(number_start, number_finish, step)
    # создаем список со значением типа строка перебирая генератор
    result_progression = list(map(str, progression))
    return result_progression


# задаем вопрос/задачу юзеру
def question(random_number_1, random_number_2='', random_sign=''):
    if random_number_2 == '':
        print(f'Question: {random_number_1}')
    elif random_sign == '':
        print(f'Question: {random_number_1} {random_number_2}')
    else:
        print(f'Question: {random_number_1} {random_sign} {random_number_2}')


# вычисляем результат для игры brain_even
def calculation_result_even(value_task):
    if value_task % 2 == 0:
        return 'yes'
    else:
        return 'no'


# получаем послед-ность простых чисел для brain_prime и проверяем ответ юзера
def calculation_result_prime(lower_number, upper_number, number_sequence_prime):
    sequence_prime_numbers = []
    # получили последовательность простых чисел от lower_number до upper_number
    for number in range(lower_number, upper_number + 1):
        if number > 1:
            for i in range(2, number):
                if (number % i) == 0:
                    break
            else:
                sequence_prime_numbers.append(number)
    return 'yes' if number_sequence_prime in sequence_prime_numbers else 'no'


def answer_user_str():
    return prompt.string('Your answer: ')


def answer_user_int():
    return prompt.integer('Your answer: ')


def checking_answer(calculation_value, answer_user_value):
    # проверяем результат even
    return True if str(calculation_value) == str(answer_user_value) else False


# вычисляем результат игры brain_calc
def expression_calculation(random_number_1, random_number_2, random_sign):
    result = eval(f'{random_number_1} {random_sign} {random_number_2}')
    return result


# вычисляем результат игры brain_gcd
def calculation_result_gcd(random_number_1, random_number_2):
    return math.gcd(random_number_1, random_number_2)


# вычисляем результат игры brain_progression
def calculation_result_progression(string_progression, random_hide_number):
    result = string_progression
    result[random_hide_number] = '..'
    return result


def display_game_result(name_user, rigth_value, answer_user_value, task_value):
    if task_value is False:
        # неправильный ответ юзера
        print(f"'{answer_user_value}' is wrong answer ;(. Correct answer was "
              f"'{rigth_value}'.\n"
              f"Let's try again, {name_user}!")
        exit()
    else:
        # правильный ответ юзера
        print('Correct!')
