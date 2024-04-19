from tabulate import tabulate
import json

def readfile():
    with open('./dish_database.json', 'r') as invent:
        table_dish = json.load(invent)
        return table_dish
    
table_dish = readfile()

def savefile():
    with open('./dish_database.json', 'w') as invent:
        json.dump(table_dish, invent)

def table():

    table_with_index = []

    for i, row in enumerate(table_dish[1:], start=1):
        indexed_row = [i] + row
        table_with_index.append(indexed_row)

    print(tabulate(table_with_index, headers=table_dish[0]))

def error_messsage():
    print("Incorrect, please enter a correct input!")

def menu_interface():
    
    print('''
    Welcome to the Kemaru-Raamen Ya
          
    1. Show Dish
    2. Add/Update Dish
    3. Delete Dish
    4. Order a Dish
    5. Exit Restaurant
    ''')

def menu_input():
    menu_inp = input("Enter a menu you want to run :")
    return menu_inp

def welcome(user):
    if user == "owner":
        print("Welcome Owner")
    elif user == "customer":
        print("Irashaimase, we have some delicious raamen special for you!")

def update_existing_dish(input_dishname):
    for dish in table_dish:
        if input_dishname == dish[0].lower():
            stock_update = int(input("Enter stock: "))
            price_update = int(input("Enter price: "))
            dish[2] = stock_update
            dish[3] = price_update
            savefile()
            print(f"Dish {input_dishname.title()} updated!")
            
    
def new_dish(input_dishname):
    input_cat = input("Enter Dish category :")
    input_stock = int(input("Enter stock :"))
    input_price = int(input("Enter price :"))
    invent_update = [input_dishname.title(), input_cat.capitalize(), input_stock, input_price]
    table_dish.append(invent_update)
    savefile()
    print("New dish added!")



    


            