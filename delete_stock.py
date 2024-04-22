import function as fn

def delete_dish():
    while True:
        choice_3 = fn.user_inp("Do you want to proceed with the dish deletion ? (yes/no) :", ["yes", "no"])
        if choice_3 == "yes":
            fn.total_dish()
            while True:
                fn.table()
                input_del = input("Enter dish index you want to delete :")
                if input_del.isalpha():
                    fn.error_message()
                    continue
                input_del = int(input_del)
                if input_del > fn.total_dish():
                    fn.error_message()
                    continue
                else:
                    break
        else:
            break
        dish_name = fn.table_dish[input_del][0]
        confirm_inp = fn.user_inp(f"Are you sure you eant to delete dish {dish_name} from the menu ? (yes/no) :", ["yes", "no"])

        if confirm_inp == "yes":
            fn.delete(input_del)
            
        elif confirm_inp == "no" or choice_3 == "no":
            print("Delete action canceled!")
    