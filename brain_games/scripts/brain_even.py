#!/usr/bin/env python3
# file <brain_even.py>

from brain_games import question_answer as qa


def main():
    qa.greeting_user()                  # приветствуем игрока
    name_user = qa.give_name()          # узнаем имя
    qa.task_to_the_user()               # объясняем задачу игроку
    for i in range(0, 3):
        number_random = qa.question()   # задаем вопрос
        # и запоминаем случайное число
        result_user = qa.answer_user(number_random)   # получаем ответ и
        # проверяем
        if result_user is False:
            print(f"yes' is wrong answer ;(. Correct answer was 'no'.\n"
                  f"Let's try again, {name_user}!")
            exit()                      # неправильный ответ юзера
        else:
            print('Correct!')
    print(f"Congratulations, {name_user}!")


if __name__ == '__main__':
    main()
