import random

RULES = 'What is the result of the expression?'
CALC_LOWER_BOUND = 1
CALC_UPPER_BOUND = 19


def get_addition(operand_first, operand_second):
    return operand_first + operand_second


def get_subtraction(operand_first, operand_second):
    return operand_first - operand_second


def get_multiply(operand_first, operand_second):
    return operand_first * operand_second


def get_question_solution(
        lower_bound=CALC_LOWER_BOUND, upper_bound=CALC_UPPER_BOUND):
    number_1 = str(random.randint(lower_bound, upper_bound))
    number_2 = str(random.randint(lower_bound, upper_bound))
    sign = ['+', '-', '*']
    choice_sign = random.choice(sign)
    question = f'{number_1} {choice_sign} {number_2}'
    symbol_function = {
        '+': get_addition,
        '-': get_subtraction,
        '*': get_multiply,
    }
    correct_answer = symbol_function[choice_sign](
        int(number_1), int(number_2))

    return question, str(correct_answer)
