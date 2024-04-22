import function as fn

def update_dish():
      
    inp2_choice = fn.user_inp("Do you want to 1. Add new dish  2. Cancel (1/2) :", ["1", "2"])
    if inp2_choice == "1":
        input_dishname = input("Enter Dish name :").lower()
        dish_exists = False

        for dish in fn.table_dish:
            if input_dishname == dish[0].lower():
                print(f"Dish {input_dishname.title()} already exists!")
                while True:
                    exists_input = fn.user_inp("Do you want to update dish instead? (yes/no) :", ["yes", "no"]).lower()
                    if exists_input == "yes":
                        fn.update_existing_dish(input_dishname)
                        dish_exists = True
                        break
                    elif exists_input == "no":
                        dish_exists = True
                        break
        
        if not dish_exists:
            fn.new_dish(input_dishname)
    elif inp2_choice == "2":
            print("Update canceled!")
            
            

