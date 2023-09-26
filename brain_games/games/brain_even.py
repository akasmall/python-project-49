# file <brain_even.py>

from brain_games import question_answer as qa


# def main():
def brain_even_game(name_user):
    # приветствуем игрока
    # qa.greeting_user()
    # узнаем имя
    # name_user = qa.give_name()
    # объясняем задачу игроку
    qa.task_to_the_user("even")
    # даем три попытки
    for i in range(0, 3):
        # запоминаем случайное число
        random_number = qa.random_number(1, 99)
        # задаем вопрос юзеру
        qa.question(random_number)
        # получаем ответ и проверяем
        result_user = qa.answer_user('even', random_number)
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


"""
if __name__ == '__main__':
    main()
"""
