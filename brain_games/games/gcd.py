"""файл игрового модуля brain_gcd_game"""
import math
import random

RULES = 'Find the greatest common divisor of given numbers.'
LOWER_BOUND = 2
UPPER_BOUND = 99


def get_question_solution(lower_bound=LOWER_BOUND, upper_bound=UPPER_BOUND):
    """ получаем строку вопроса и результат задачи brain_gcd_game"""
    number_1 = random.randint(lower_bound, upper_bound)
    number_2 = random.randint(lower_bound, upper_bound)
    question = f'{number_1} {number_2}'
    correct_answer = math.gcd(number_1, number_2)

    return question, correct_answer
