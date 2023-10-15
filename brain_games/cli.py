"""начальное задание проекта"""
import prompt


def welcome_user():
    """просто привествуем"""
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
