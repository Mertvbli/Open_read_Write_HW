from pprint import pprint


def cook_file():
    with open("recipe.txt", encoding='utf-8') as file:
        cook_book = {}
        for dish in file:
            dish_name = dish.strip()
            counter = int(file.readline().strip())
            elem_list = []
            for item in range(counter):
                ingredient_name, quantity, measure = file.readline().strip().split(' | ')
                elem_list.append({
                    'ingredient_name': ingredient_name, 'quantity': int(quantity), 'measure': measure.replace('\n', '')
                })
            cook_book[dish_name] = elem_list
            file.readline()
    return cook_book


def get_shop_list_by_dishes(dishes, person_count, book = cook_file()):
    full = {}
    for i in dishes:
        for j in book[i]:
            if j['ingredient_name'] in full.keys():
                full[j['ingredient_name']]['quantity'] += j['quantity'] * person_count
            else:
                full[j['ingredient_name']] = {}
                full[j['ingredient_name']]['measure'] = j['measure']
                full[j['ingredient_name']]['quantity'] = j['quantity'] * person_count
    return full


pprint(get_shop_list_by_dishes(['Омлет', 'Омлет'], 3))
