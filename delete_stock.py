import access as acc
import show_table as table

def input_3():
    choice_3 = input("Do you want to proceed with the dish deletion ? (yes/no) :")
    choice_3_low = choice_3.lower()
    while choice_3_low == "yes":
            dish_count = len(acc.table_dish) - 1

            while True:
                table.table()
                input_del = input("Enter dish index you want to delete :")
                if not input_del.isdigit():
                     print("Enter an index of a dish!")
                else:
                    index_del = int(input_del)
                    if index_del > dish_count:
                         print("Enter a correct index!")
                    else:
                         break

            dish_name = acc.table_dish[index_del][0]
            confirm_inp = input(f"Are you sure you eant to delete dish {dish_name} from the menu ? (1. Yes 2. No) :")

            if confirm_inp in ["Yes", "yes", 1, "1"]:
                del acc.table_dish[index_del]
                acc.savefile()
                print(f"Dish {dish_name} successfuly deleted!")
                break
            elif confirm_inp in ["No", "no", "2", 2]:
                print("Delete action canceled!")
                break
    while choice_3_low == "no":
         break
        