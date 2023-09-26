#!/usr/bin/env python3
# file <brain_calc.py>

from brain_games import question_answer as qa


def main():
    # приветствуем игрока
    qa.greeting_user()
    # узнаем имя юзера
    name_user = qa.give_name()
    # объясняем задачу игроку
    qa.task_to_the_user("gcd")
    # даем три попытки
    for i in range(0, 3):
        # определяем случайный знак
        # random_sign = qa.random_sign(['+', '-', '*'])
        # получаем и запоминаем два случайных числа
        random_number_1 = qa.random_number(1, 99)
        random_number_2 = qa.random_number(1, 99)
        # вычисляем выражение игры
        calculation_result = qa.calculation_result_gcd(random_number_1,
                                                       random_number_2
                                                       )
        # print(calculation_result)
        # задаем задачу юзеру вычислить
        qa.question(random_number_1, random_number_2)
        # получаем ответ и проверяем
        result_user = qa.answer_user('gcd', calculation_result)
        if result_user is False:
            # неправильный ответ юзера
            print(f"yes' is wrong answer ;(. Correct answer was 'no'.\n"
                  f"Let's try again, {name_user}!")
            exit()
        else:
            # правильный ответ юзера
            print('Correct!')
    # поздравляем юзера
    print(f"Congratulations, {name_user}!")


if __name__ == '__main__':
    main()
