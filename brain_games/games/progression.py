"""файл игрового модуля brain_progression_game"""
import random

RULES = 'What number is missing in the progression?'
# LEN_SEQUENCE = 10
LOWER_BOUND_A1 = 1
UPPER_BOUND_A1 = 19
LOWER_BOUND_D = 1
UPPER_BOUND_D = 9
LEN_PROGRESSION = 10


def get_question_solution(
        lower_bound_a1=LOWER_BOUND_A1, upper_bound_a1=UPPER_BOUND_A1,
        lower_bound_d=LOWER_BOUND_D, upper_bound_d=UPPER_BOUND_D,
        len_progression=LEN_PROGRESSION):
    """ получаем строку вопроса и правильный результат brain_progression"""
    a1_progression = random.randint(lower_bound_a1, upper_bound_a1)
    d_progression = random.randint(lower_bound_d, upper_bound_d)
    an_progression = a1_progression + len_progression * d_progression
    progression = range(a1_progression, an_progression, d_progression)
    str_progression = list(map(str, progression))
    index_hide = random.randint(lower_bound_d, upper_bound_d)
    # # прячем число прогрессии
    str_progression[index_hide] = '..'
    question = " ".join(str_progression)
    # return str_progression, d_progression, index_hide
    if index_hide + 1 < len(str_progression):
        correct_answer = int(
            str_progression[index_hide + 1]) - d_progression
    else:
        correct_answer = int(
            str_progression[index_hide - 1]) + d_progression

    return question, correct_answer
