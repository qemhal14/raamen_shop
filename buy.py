from tabulate import tabulate
import function as fn

def input_4():
    cart_head = [["Dish", "Quantity", "Price"]] 
    total_price = 0
    dish_count = len(fn.table_dish) - 1
    
    while True:
        fn.table()
        input_buy = input("Enter dish index you want to order :")

        try:
            input_buy = int(input_buy)
        except ValueError:
            print("Please enter a correct index menu! ")
            continue

        if input_buy > dish_count:
            print("Enter a correct index!")
            continue
        
        while True:
            input_qty = input("Enter quantity :")
            try:
                input_qty = int(input_qty)
                break
            except ValueError:
                print("Please enter a valid number for the quantity!")
                continue

        dish_picked = fn.table_dish[input_buy]
        stock_dish_picked = dish_picked[2]
        price_dish_picked = dish_picked[3] 

        if input_qty <= stock_dish_picked:
            subtotal_price = input_qty * price_dish_picked
            cart = [dish_picked[0], input_qty, subtotal_price]
            total_price += subtotal_price
            cart_head.append(cart)
            print(tabulate(cart_head))
            # Update stock
            fn.table_dish[input_buy][2] -= input_qty
            add_another = input("Do you like to add antoher dish? (yes/no) :").lower()
            fn.savefile()
            
            while add_another not in ["yes", "no"]:
                add_another = input("Do you like to add antoher dish? (yes/no) :").lower()

            if add_another == "yes":
                continue
            
            elif add_another == "no":
                print(tabulate(cart_head))
                print("Here is the sum of your order", total_price)
                if total_price > 150000:
                    get_cb = True
                    print("Your order is above Rp 150.000, you got 10% Cashback!")
                    print("Apply 'GET10CB' below for the Cashback!")

                    while True:
                        cb_inp = input("Enter code here :")
                        if cb_inp == "GET10CB":
                            print("Voucher successfuly applied!")
                            price_after_cb = total_price - (total_price * 0.1)
                            print("Here is the sum of your order after Cashback", price_after_cb)
                            break
                        else:
                            print("Voucher not matched!")
                            continue

                else:
                    get_cb = False

                while get_cb == True:
                    payment = int(input("Enter money :"))
                    if payment < price_after_cb:
                        print("Transaction cannot continue, your money is not enough!")
                        print("Your money is short",price_after_cb - payment)
            
                    elif payment == price_after_cb:
                        print("Thank you for ordering, please wait while we prepare your food :)")
                        break
            
                    else:
                        print("Thank you for ordering, please wait while we prepare your food :)")
                        print(payment - price_after_cb, "is your change.")
                        break
                while get_cb == False:
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