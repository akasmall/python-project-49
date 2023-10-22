"""общий модуль логики игр"""
import prompt

NUMBER_ROUNDS = 3


def launch_game(game):
    """запускаю игру """
    print('Welcome to the Brain Games!')
    # узнаем имя
    name_user = prompt.string('May I have your name? ')
    print(f'Hello, {name_user}!')
    # объясняем задачу игроку
    print(game.RULES)
    # задаем три задачи
    for _ in range(NUMBER_ROUNDS):
        # получаем значение для вопроса и вычисляем правильнй результат игры
        question, correct_answer = game.get_question_solution()
        # print(f'Вычисленный ответ: {solution}')
        # задаем вопрос юзеру
        print(f'Question: {question}')
        # получаем ответ от юзера
        answer_user = prompt.string('Your answer: ')
        # проверяем ответ от юзер
        if str(correct_answer) != str(answer_user):
            # неправильный ответ юзера
            print(f"'{answer_user}' is wrong answer ;(. "
                  f"Correct answer was "
                  f"'{correct_answer}'.\n"
                  f"Let's try again, {name_user}!")
            exit()
        else:
            print('Correct!')
    print(f"Congratulations, {name_user}!")
