"""Логика игр."""
import math
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


def task_to_the_user(name_game):
    """объясняем задание юзеру."""
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


def random_sign(sign):
    """
    получаем случайный знак из списка
    а также получаем случайное число для prime.
    """
    random.shuffle(sign)
    return random.choice(sign)


def random_number(number_1, number_2):
    """получаем случайное число."""
    return random.randint(number_1, number_2)


def random_progression(number_start, number_finish, step):
    """получаем случайную прогрессию со случайным шагом."""
    # получаем ссылку на генератор от до и шагом
    progression = range(number_start, number_finish, step)
    # создаем список со значением типа строка перебирая генератор
    # result_progression = list(map(str, progression))
    # return result_progression
    return list(map(str, progression))


def question(random_number_1, random_number_2='', random_sign_question=''):
    """задаем вопрос/задачу юзеру."""
    if random_number_2 == '':
        print(f'Question: {random_number_1}')
    elif random_sign_question == '':
        print(f'Question: {random_number_1} {random_number_2}')
    else:
        print(f'Question: {random_number_1} '
              f'{random_sign_question} {random_number_2}')


def calculation_result_even(value_task):
    """вычисляем результат для игры brain_even."""
    return 'yes' if value_task % 2 == 0 else 'no'


def getting_sequence_prime_numbers(lower_number,
                                   upper_number):
    """
    получили последовательность простых чисел от lower_number до upper_number.
    """
    sequence_prime_numbers = []
    for number in range(lower_number, upper_number + 1):
        if number > 1:
            for i in range(2, number):
                if (number % i) == 0:
                    break
            else:
                sequence_prime_numbers.append(number)
    return sequence_prime_numbers


def calculation_result_prime(lower_number, upper_number,
                             number_sequence_prime):
    """
    получаем последовательность простых чисел для brain_prime и
    проверяем ответ юзера.
    """
    sequence_prime_numbers = getting_sequence_prime_numbers(
        lower_number,
        upper_number)
    return 'yes' if number_sequence_prime in sequence_prime_numbers else 'no'


def answer_user():
    """получаем ответ от пользователя."""
    return prompt.string('Your answer: ')


# def answer_user_str():
#     return prompt.string('Your answer: ')


# def answer_user_int():
#     return prompt.integer('Your answer: ')


def checking_answer(calculation_value, answer_user_value):
    """проверяем результат even."""
    return True if str(calculation_value) == str(answer_user_value) else False


def calc_plus(operand_first, operand_second):
    """ вычисляем в игре калькулятор сумму. """
    return operand_first + operand_second


def calc_minus(operand_first, operand_second):
    """ вычисляем в игре калькулятор разницу. """
    return operand_first - operand_second


def calc_multiply(operand_first, operand_second):
    """ вычисляем в игре калькулятор умножение. """
    return operand_first * operand_second


def expression_calculation(random_number_1, random_number_2, random_sign_calc):
    """вычисляем результат игры brain_calc."""
    dist_sign = {
        '+': calc_plus,
        '-': calc_minus,
        '*': calc_multiply,
    }
    if dist_sign.get(random_sign_calc, False) is not False:
        return dist_sign[random_sign_calc](random_number_1, random_number_2)
    else:
        print('Something went wrong!')
        exit()


def calculation_result_gcd(random_number_1, random_number_2):
    """вычисляем результат игры brain_gcd."""
    return math.gcd(random_number_1, random_number_2)


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
