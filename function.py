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
    table= []
    for i, row in enumerate(table_dish[1:], start=1):
        indexed_row = [i] + row
        table.append(indexed_row)
    print(tabulate(table, headers=table_dish[0]))

def sort_table(table, options):
    if options == "category":
        sorted_table = sorted(table[1:], key=lambda x: x[1])
    elif options == "price":
        sorted_table = sorted(table[1:], key=lambda x: x[3])
    else:
        raise ValueError("Invalid sort option. Please choose 'category' or 'price'.")
    return sorted_table

def sort_category():
    sorted_table_by_category = sort_table(table_dish, "category")
    print(tabulate(sorted_table_by_category, headers=table_dish[0]))

def sort_price():
    sorted_table_by_price = sort_table(table_dish, "price")
    print(tabulate(sorted_table_by_price, headers=table_dish[0]))

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
            dish[2] += stock_update
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

def user_inp(prompt, options):
    user_input = input(prompt)
    while user_input not in options:
        print("Invalid input!")
        user_input = input(prompt)
    return user_input

def total_dish():
    dish_count = len(table_dish) - 1
    return dish_count

def delete(input_del):
    del table_dish[input_del]
    savefile()
    print("Dish successfuly deleted!")

def error_message():    
    print("Invalid input!")

    


            