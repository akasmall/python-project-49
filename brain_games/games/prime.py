import random

RULES = 'Answer "yes" if given number is prime. Otherwise answer "no".'
PRIME_LOWER_BOUND = 1
PRIME_UPPER_BOUND = 99


def is_number_prime(number):
    if number < 2:
        return False
    divisor = 2
    while divisor <= number / 2:
        if not number % divisor:
            return False
        divisor += 1
    return True


def gets_question_solution(
        lower_bound=PRIME_LOWER_BOUND, upper_bound=PRIME_UPPER_BOUND):
    number = random.randint(lower_bound, upper_bound)
    if is_number_prime(number):
        correct_answer = 'yes'
    else:
        correct_answer = 'no'

    return str(number), correct_answer
