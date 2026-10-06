# Проект FitLife - MVP версия 1.0
from math import pow

WATER_PER_KG = 30
ML_IN_L = 1000

print('Добро пожаловать в приложение FitLife!')

user_name = input('Пожалуйста, представьтесь (укажите имя): ').title()
user_age = int(input('Укажите сколько вам лет (полных лет, наприер 22): '))
questions = ['Укажите ваш вес (в кг, например 67.5): ',
             'Укажите ваш рост (в метрах, например 1.75): ']
user_weight = float(input(questions[0]).replace(',', '.'))
user_height = float(input(questions[1]).replace(',', '.'))


def calculate_bmi(user_weight: float, user_height: float) -> float:
    """Вычисляет ИМТ пользователя.

    Основные аргументы:
    user_weight -- вес пользователя
    user_height -- рост пользователя
    """
    return user_weight / pow(user_height, 2)


bmi = round(calculate_bmi(user_weight, user_height), 1)

water_needed_in_ml = user_weight * WATER_PER_KG
water_needed_in_l = water_needed_in_ml / ML_IN_L

print('')
print(f'Привет, {user_name}!')
print('Ваши показатели:')
print(f'Возраст: {user_age}, ИМТ: {bmi},', end=' ')
print(f'Норма воды в день: {water_needed_in_l:.1f} л.')
print("Расчет окончен. Будьте здоровы!")
