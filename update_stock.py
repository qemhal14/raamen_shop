import access as acc
import show_table as table


def input_2():
      
    while True:
        inp2_choice = input("Do you want to 1. Update dish 2. Add new dish  3. Cancel (1/2/3) :")
        if inp2_choice == "1":
            update_dish()
            
            
        elif inp2_choice == "2":
            input_dishname = input("Enter Dish name :")
            dishname_low = input_dishname.lower()
            dish_exists = False

            for row in acc.table_dish:
                if dishname_low == row[0].lower():
                    print(f"Dish {dishname_low.title()} already exists!")
                    exists_input = input("Do you want to update dish instead? (yes/no) :")
                    exists_conv = exists_input.lower()
                    if exists_conv == "yes":
                        update_dish()
                    else:
                        dish_exists = True
                        break
            
            if not dish_exists:
                input_cat = input("Enter Dish category :")
                input_stock = int(input("Enter stock :"))
                input_price = int(input("Enter price :"))
                invent_update = [input_dishname.title(), input_cat.capitalize(), input_stock, input_price]
                acc.table_dish.append(invent_update)
                acc.savefile()
                print("New dish added!")
        
        elif inp2_choice == "3":
             print("Update canceled!")
             break

def update_dish():
    while True:
        dish_count = len(acc.table_dish) - 1

        while True:
            table.table()
            input_index = input("Enter index dish you want to update :")
            if not input_index.isdigit():
                print("Enter an index of a Dish")
            else:
                input_index = int(input_index)
                if input_index > dish_count:
                    print("Enter a correct index!")
                else:
                    break
                
        get_index = int(input_index)
        dish_info = acc.table_dish[get_index]
        print(f"Dish name :{dish_info[0]}\nType dish :{dish_info[1]}\nAvailable :{dish_info[2]}\nPrice :{dish_info[3]}")
        con_update = input("Dou you want to continue update? (yes/no) :")
        con_update_low = con_update.lower()
    
        if con_update_low == "no":
            break
        elif con_update_low == "yes":
            
            dishname_update = input("Enter a dish name :")
            cat_update = input("Enter a dish category :")
            stock_update = int(input("Enter stock :"))
            price_update = int(input("Enter price :"))

            acc.table_dish[get_index][0] = dishname_update.title()
            acc.table_dish[get_index][1] = cat_update.capitalize()
            acc.table_dish[get_index][2] += stock_update
            acc.table_dish[get_index][3] = price_update
            acc.savefile()
            print("Dish updated!")
            
    