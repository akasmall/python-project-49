"""общий модуль логики игр"""
import prompt

NUMBER_ROUNDS = 3


# def started_finished(logic_module):
def start_game(logic_module):
    """запускаю игру """
    print('Welcome to the Brain Games!')
    # узнаем имя
    name_user = prompt.string('May I have your name? ')
    print(f'Hello, {name_user}!')
    # объясняем задачу игроку
    print(logic_module.TASK_USER)
    # задаем три задачи
    for _ in range(NUMBER_ROUNDS):
        # получаем значение для вопроса и вычисляем правильнй результат игры
        question, solution_task = logic_module.get_question_solution()
        # print(f'Вычисленный ответ: {solution_task}')
        # задаем вопрос юзеру
        print(f'Question: {question}')
        # получаем ответ от юзера
        answer_user = prompt.string('Your answer: ')
        # проверяем ответ от юзер
        result_task = True if str(solution_task) == str(
            answer_user) else False
        if result_task is False:
            # неправильный ответ юзера
            print(f"'{answer_user}' is wrong answer ;(. "
                  f"Correct answer was "
                  f"'{solution_task}'.\n"
                  f"Let's try again, {name_user}!")
            exit()
        else:
            print('Correct!')
    print(f"Congratulations, {name_user}!")
