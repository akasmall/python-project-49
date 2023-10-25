import prompt

NUMBER_ROUNDS = 3


def launch_game(game):
    print('Welcome to the Brain Games!')
    name_user = prompt.string('May I have your name? ')
    print(f'Hello, {name_user}!')
    print(game.RULES)
    for _ in range(NUMBER_ROUNDS):
        question, correct_answer = game.get_question_solution()
        print(f'Question: {question}')
        answer_user = prompt.string('Your answer: ')
        if str(correct_answer) != str(answer_user):
            print(f"'{answer_user}' is wrong answer ;(. "
                  f"Correct answer was "
                  f"'{correct_answer}'.\n"
                  f"Let's try again, {name_user}!")
            exit()
        else:
            print('Correct!')
    print(f"Congratulations, {name_user}!")
