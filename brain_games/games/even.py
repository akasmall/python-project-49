import random

RULES = 'Answer "yes" if the number is even, otherwise answer "no".'
EVEN_LOWER_BOUND = 1
EVEN_UPPER_BOUND = 99


def is_number_even(number):
    return number % 2


def gets_question_solution(
        lower_bound=EVEN_LOWER_BOUND, upper_bound=EVEN_UPPER_BOUND):
    number = random.randint(lower_bound, upper_bound)
    if is_number_even(number):
        correct_answer = 'no'
    else:
        correct_answer = 'yes'
    return str(number), correct_answer
