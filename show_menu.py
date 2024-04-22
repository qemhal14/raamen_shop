import buy as buy
import function as fn

def menu_options():
    print(
    '''
        
    Menu options :
    1. Sort by category
    2. Sort by price
    3. Order a menu
    4. Back to main menu
        ''')

def menu():
    fn.table()
    while True:
        menu_options()
        input_1 = fn.user_inp("Input a menu you want to run (1/2/3/4):", ["1", "2", "3", "4"])

        if input_1 == "1":
            fn.sort_category()
            continue
        elif input_1 == "2":
            fn.sort_price()
            continue
        elif input_1 == "3":
            buy.order()
            break
        elif input_1 == "4":
            break
        
      