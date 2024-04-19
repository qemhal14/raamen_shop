import function as fn

def input_3():
    choice_3 = input("Do you want to proceed with the dish deletion ? (yes/no) :").lower()
    while choice_3 not in ["yes", "no"]:
         print("Please enter yes or no!")
         choice_3 = input("Do you want to proceed with the dish deletion ? (yes/no) :").lower()
    
    if choice_3 == "yes":
            dish_count = len(fn.table_dish) - 1 #excluding the headers

            while True:
                fn.table()
                input_del = input("Enter dish index you want to delete :")
                if not input_del.isdigit():
                     print("Enter an index of a dish!")
                else:
                    index_del = int(input_del)
                    if index_del > dish_count:
                         print("Please enter a correct index!")
                    else:
                         break

            dish_name = fn.table_dish[index_del][0]
            confirm_inp = input(f"Are you sure you eant to delete dish {dish_name} from the menu ? (yes/no) :").lower()
            while confirm_inp not in ["yes", "no"]:
                print("Please enter yes or no!")
                confirm_inp = input(f"Are you sure you eant to delete dish {dish_name} from the menu ? (yes/no) :").lower()

            if confirm_inp == "yes":
                del fn.table_dish[index_del]
                fn.savefile()
                print(f"Dish {dish_name} successfuly deleted!")
                
            elif confirm_inp == "no":
                print("Delete action canceled!")
                
    elif choice_3 == "no":
         print("Action canceled!")
        