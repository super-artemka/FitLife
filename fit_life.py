# Проект FitLife - MVP версия 1.0
from math import pow

WATER_PER_KG = 30
ML_IN_L = 1000

# 1. Знакомство
# TODO: Спроси у пользователя имя и сохрани в переменную user_name
# TODO: Спроси возраст и сохрани в переменную user_age
# TODO: (не забудь преобразовать в число)

print('Добро пожаловать в приложение FitLife!')
user_name = input('Пожалуйста, представьтесь: ')
user_age = int(input('Укажите сколько вам лет: '))

# 2. Сбор данных
# TODO: Запроси вес (в кг) и сохрани в user_weight (тип float)
# TODO: Запроси рост (в метрах, например 1.75)
# TODO: И сохрани в user_height (тип float)

user_weight = float(input('Укажите ваш вес (в кг, например 67.5): '))
user_height = float(input('Укажите ваш рост (в метрах, например 1.75): '))

# 3. Логика расчетов (Функции как "черный ящик": используем арифметику)
# Формула ИМТ: вес разделить на (рост в квадрате)
# TODO: Рассчитай bmi (Индекс массы тела)


def calculate_bmi(user_weight: float, user_height: float) -> float:
    return user_weight / pow(user_height, 2)


bmi = round(calculate_bmi(user_weight, user_height), 1)

# Подсчет воды: вес * 30 мл
# TODO: Рассчитай water_needed

water_needed_in_ml = user_weight * WATER_PER_KG
water_needed_in_l = water_needed_in_ml / ML_IN_L

# 4. Вывод красивого результата
# TODO: Используй f-строку, чтобы вывести приветствие,
# TODO: Например: "Привет, Иван!"
# TODO: Выведи возраст, ИМТ (округленный до 1 знака) и норму воды.

print('')
print(f'Привет, {user_name}!')
print('Ваши показатели:')
print(f'Возраст: {user_age}, ИМТ: {bmi},', end=' ')
print(f'Норма воды в день: {water_needed_in_l:.1f} л.')
print("Расчет окончен. Будьте здоровы!")
