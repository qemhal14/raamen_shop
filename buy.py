from tabulate import tabulate
import function as fn

def cashback_message():
    print("Your order is above Rp 150000, you get 10% Cashback!")
    print("Apply 'GET10CB' below for the Cashback!")

def calculate_total_price(cart_head):
    total_price = sum(row[2] for row in cart_head[1:])
    return total_price

def display_order_summary(cart_head, total_price):
    print(tabulate(cart_head))
    print("Here is the sum of your order:", total_price)

def process_order(total_price):
    if total_price > 150000:
        cashback_message()
        voucher = fn.user_inp("Enter code here: ","GET10CB")
        if voucher == "GET10CB":
            total_price *= 0.9
            print("Here is the sum of your order after Cashback:", total_price)
    return total_price

def get_payment(total_price):
    while True:
        payment = int(input("Enter money: "))
        if payment < total_price:
            print("Transaction cannot continue, your money is not enough!")
            print("Your money is short", total_price - payment)
        else:
            change = payment - total_price
            if change > 0:
                print(change, "is your change.")
            print("Thank you for ordering, please wait while we prepare your food :)")
            break

def update_stock(cart_head):
    for item in cart_head[1:]:
        dish_name = item[0]
        for i, row in enumerate(fn.table_dish):
            if row[0] == dish_name:
                fn.table_dish[i][2] -= item[1]
                break
    fn.savefile()

def order():
    fn.total_dish()
    cart_head = [["Dish", "Quantity", "Price"]]

    while True:
        fn.table()
        try:
            input_buy = int(input("Enter dish index you want to order: "))
            if input_buy < 0 or input_buy > fn.total_dish():
                fn.error_message()
                continue
            dish_ordered = fn.table_dish[input_buy]
            dishname_ordered = dish_ordered[0]
            stock_ordered = dish_ordered[2]
            price_ordered = dish_ordered[3]
        except ValueError:
            fn.error_message()
            continue

        while True:
            try:
                input_qty = int(input("Enter quantity: "))
                if input_qty <= stock_ordered:
                    break
                print(f"{dishname_ordered} stock is not enough! Stock remaining: {stock_ordered}.")
            except ValueError:
                fn.error_message()
                continue

        subtotal_price = input_qty * price_ordered
        cart = [dishname_ordered, input_qty, subtotal_price]
        cart_head.append(cart)
        print(tabulate(cart_head))

        add_another = fn.user_inp("Do you like to add another dish? (yes/no): ", ["yes", "no"]).lower()
        if add_another == "no":
            total_price = calculate_total_price(cart_head)
            display_order_summary(cart_head, total_price)
            total_price = process_order(total_price)
            get_payment(total_price)
            update_stock(cart_head)
            break

