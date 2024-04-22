import show_menu as showmenu
import update_stock as update
import delete_stock as delete
import buy as buy
import function as fn

user = fn.user_inp("Dou you want to continue as (owner/customer) :", ["owner", "customer"]).lower()
user_login = False
    
if user == "owner":
    password = fn.user_inp("Please enter password :", ["admin"])
    user_login = True
elif user == "customer":
    user_login = True

def menu_interface():
    
    print('''
    Welcome to the Kemaru-Raamen Ya
          
    1. Show Dish
    2. Add/Update Dish
    3. Delete Dish
    4. Order a Dish
    5. Exit Restaurant
    ''')

while user_login == True:

    fn.welcome(user)
    menu_interface()
    menu_inp = fn.user_inp("Enter a menu you want to run :", ["1", "2", "3", "4", "5"])
        
    if menu_inp == "1":
        showmenu.menu()

    elif menu_inp == "2" and user == "owner":
        update.update_dish()
    elif menu_inp == "2" and user == "customer":
        print("Sorry this feature only available for owner")
         
    elif menu_inp == "3" and user == "owner":
        delete.delete_dish()
    elif menu_inp == "3" and user == "customer":
        print("Sorry this feature only available for owner")

    elif menu_inp == "4":
        buy.order()

    elif menu_inp == "5":
        print("Arigato Gozaimashita!")
        break
            

