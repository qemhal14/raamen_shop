import json

def readfile():
    with open('raamen_shop/dish_database.json', 'r') as invent:
        table_dish = json.load(invent)
        return table_dish
    
table_dish = readfile()

def savefile():
    with open('raamen_shop/dish_database.json', 'w') as invent:
        json.dump(table_dish, invent)