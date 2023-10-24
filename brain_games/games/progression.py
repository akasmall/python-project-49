import random

RULES = 'What number is missing in the progression?'
PROGRESSION_LOWER_BOUND_A1 = 1
PROGRESSION_UPPER_BOUND_A1 = 19
PROGRESSION_LOWER_BOUND_D = 1
PROGRESSION_UPPER_BOUND_D = 9
PROGRESSION_LEN = 10


def gets_progression(a1_progression, an_progression, d_progression):
    progression = range(a1_progression, an_progression, d_progression)
    str_progression = list(map(str, progression))
    return str_progression


def gets_quastion(str_progression, index_hide):
    str_progression[index_hide] = '..'
    return " ".join(str_progression)


def gets_question_solution(
        lower_bound_a1=PROGRESSION_LOWER_BOUND_A1,
        upper_bound_a1=PROGRESSION_UPPER_BOUND_A1,
        lower_bound_d=PROGRESSION_LOWER_BOUND_D,
        upper_bound_d=PROGRESSION_UPPER_BOUND_D,
        len_progression=PROGRESSION_LEN):
    a1_progression = random.randint(lower_bound_a1, upper_bound_a1)
    d_progression = random.randint(lower_bound_d, upper_bound_d)
    an_progression = a1_progression + len_progression * d_progression
    str_progression = gets_progression(
        a1_progression, an_progression, d_progression)

    index_hide = random.randint(lower_bound_d, upper_bound_d)
    correct_answer = str_progression[index_hide]
    question = gets_quastion(str_progression, index_hide)
    return question, correct_answer
