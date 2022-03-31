
cook_book = {}
with open('recept.txt', 'r', encoding='utf-8') as file:
    for i in range(4):
        q = file.readline().strip()
        cook_book[q] = []
        w = file.readline().strip()
        for i in range(int(w)):
            r = file.readline().strip().replace('|', ',').split(',')
            cook_book[q].append({'ingredient_name': r[0], 'quantity': int(r[1]), 'measure': r[2]})
        file.readline().strip()

def get_shop_list_by_dishes(dishes, person_count):
    a = {}
    for el in cook_book:
        if el in dishes:
            for e in cook_book[el]:
                if e['ingredient_name'] in a:
                    b = a[e['ingredient_name']]['quantity']
                    a[e['ingredient_name']] = {'measure' : e['measure'], 'quantity' : e['quantity'] * person_count + b}
                else:
                    a[e['ingredient_name']] = {'measure' : e['measure'], 'quantity' : e['quantity'] * person_count}
    print(a)

get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 3)