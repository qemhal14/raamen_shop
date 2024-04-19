import show_menu as showmenu
import update_stock as update
import delete_stock as delete
import buy as buy
import function as fn

user = input("Dou you want to continue as (owner/customer) :").lower()
user_login = False
while True:
    
    if user == "owner":
        password = input("Please enter password :")
        if password == "admin":
                user_login = True
                break
        else:
            fn.error_messsage()
            continue
    elif user == "customer":
        user_login = True
        break
    elif user not in ["owner", "customer"]:
        continue

while user_login == True:

    fn.welcome(user)
    fn.menu_interface()
    menu_input = fn.menu_input() 
        
    if menu_input == "1":
        showmenu.menu()

    elif menu_input == "2" and user == "owner":
        update.input_2()
    elif menu_input == "2" and user == "customer":
        print("Sorry this feature only available for owner")
         
    elif menu_input == "3" and user == "owner":
        delete.input_3()
    elif menu_input == "3" and user == "customer":
        print("Sorry this feature only available for owner")

    elif menu_input == "4":
        buy.input_4()

    elif menu_input == "5":
        print("Arigato Gozaimashita!")
        break
            
    else:
        fn.error_messsage()

