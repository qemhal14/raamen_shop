import update_stock as update
import buy as buy
import delete_stock as delete
import interface as menu
import show_menu as showmenu

user = input("Dou you want to continue as (owner/customer) :")
user_inp = user.lower()
user_login = False

while True:
    user_login = False 
    if user_inp == "owner":
        password = input("Please enter password :")

        if password == "admin":
                print("Welcome owner!")
                user_login = True
                break
    elif user_inp == "customer":
        print("Welcome customer!")
        user_login = True
        break
    elif user_inp not in ["owner", "customer"]:
        print("Please input owner or customer!")
        user = input("Dou you want to continue as (owner/customer) :")
        user_inp = user.lower()
    else:
        print("Please enter a correct password!")

while user_login == True:

    if user_inp == "owner":
        print("Good Morning Owner, let's cook some dish!")
    elif user_inp == "customer":
        print("いらっしゃいませ/Irashaimase, we have some delicious raamen special for you!")

    menu.menu_interface()
    menu_input = menu.menu_input() 
        
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
        print("Input a correct index!")   



        
        


    

