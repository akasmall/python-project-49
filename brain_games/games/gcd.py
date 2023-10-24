import math
import random

RULES = 'Find the greatest common divisor of given numbers.'
GCD_LOWER_BOUND = 2
GCD_UPPER_BOUND = 99


def gets_question_solution(
        lower_bound=GCD_LOWER_BOUND, upper_bound=GCD_UPPER_BOUND):
    number_1 = random.randint(lower_bound, upper_bound)
    number_2 = random.randint(lower_bound, upper_bound)
    question = f'{number_1} {number_2}'
    correct_answer = math.gcd(number_1, number_2)

    return question, correct_answer
