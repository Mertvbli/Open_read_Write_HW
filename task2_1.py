# 2 Task
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


def get_shop_list_by_dishes(dishes, person_count):
    full = {}
    for i in dishes:
        for j in cook_book[i]:
            if j['ingredient_name'] in full.keys():
                full[j['ingredient_name']]['quantity'] += j['quantity']
            else:
                full[j['ingredient_name']] = {}
                full[j['ingredient_name']]['measure'] = j['measure']
                full[j['ingredient_name']]['quantity'] = j['quantity'] * person_count
    return full


print(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2))
