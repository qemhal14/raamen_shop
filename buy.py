from tabulate import tabulate
import access as acc
import show_table as table

def input_4():
    cart_head = [["Dish", "Quantity", "Price"]] 
    total_price = 0
    dish_count = len(acc.table_dish) - 1
    
    while True:
        print("Our Menu")
        table.table()
        input_buy = int(input("Enter dish index you want to order :")) 

        while input_buy > dish_count:
            print("Enter a correct index!")
            input_buy = int(input("Enter dish index you want to order :"))  
        
        input_qty = int(input("Enter quantity :"))

        dish_picked = acc.table_dish[input_buy]
        stock_dish_picked = dish_picked[2]
        price_dish_picked = dish_picked[3] 

        if input_qty <= stock_dish_picked:
            subtotal_price = input_qty * price_dish_picked
            cart = [dish_picked[0], input_qty, subtotal_price]
            total_price += subtotal_price
            cart_head.append(cart)
            print(tabulate(cart_head))
            # Update stock
            acc.table_dish[input_buy][2] -= input_qty
            add_another = input("Do you like to add antoher dish? (yes/no) :")
            add_input = add_another.lower()
            acc.savefile()
            
            while add_input not in ["yes", "no"]:
                add_another = input("Do you like to add antoher dish? (yes/no) :")
                add_input = add_another.lower()

            if add_input == "yes":
                continue
            
            elif add_input == "no":
                print(tabulate(cart_head))
                print("Here is the sum of your order", total_price)

                while True:
                    payment = int(input("Enter money :"))
                    if payment < total_price:
                        print("Transaction cannot continue, your money is not enough!")
                        print("Your money is short",total_price - payment)
            
                    elif payment == total_price:
                        print("Thank you for ordering, please wait while we prepare your food :)")
                        break
            
                    else:
                        print("Thank you for ordering, please wait while we prepare your food :)")
                        print(payment - total_price, "is your change.")
                        break
            else:
                print("please input yes or no")
            break
        else:
            print(f"{dish_picked[0]} stock is not enough! stock remain is {dish_picked[2]}.")