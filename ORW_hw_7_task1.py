# 1 Task
from pprint import pprint
import os

cook_book = {
  'Омлет': [
    {'ingredient_name': 'Яйцо', 'quantity': 2, 'measure': 'шт.'},
    {'ingredient_name': 'Молоко', 'quantity': 100, 'measure': 'мл'},
    {'ingredient_name': 'Помидор', 'quantity': 2, 'measure': 'шт'}
    ],
  'Утка по-пекински': [
    {'ingredient_name': 'Утка', 'quantity': 1, 'measure': 'шт'},
    {'ingredient_name': 'Вода', 'quantity': 2, 'measure': 'л'},
    {'ingredient_name': 'Мед', 'quantity': 3, 'measure': 'ст.л'},
    {'ingredient_name': 'Соевый соус', 'quantity': 60, 'measure': 'мл'}
    ],
  'Запеченный картофель': [
    {'ingredient_name': 'Картофель', 'quantity': 1, 'measure': 'кг'},
    {'ingredient_name': 'Чеснок', 'quantity': 3, 'measure': 'зубч'},
    {'ingredient_name': 'Сыр гауда', 'quantity': 100, 'measure': 'г'},
    ]
  }

path = os.path.join(os.getcwd(), 'recipe.txt')

with open(path, encoding='utf-8') as file:
    result = {}
    for dish in file:
        dish_name = dish.strip()
        counter = int(file.readline().strip())
        elem_list = []
        for item in range(counter):
            ingredient_name, quantity, measure = file.readline().strip().split('|')
            elem_list.append(
                {'ingredient_name': ingredient_name, 'quantity': quantity, 'measure': measure}
            )
        result[dish_name] = elem_list
        file.readline()
    print(result)
