import buy as buy
import function as fn

def menu():
    while True:
        print("Our Menu")
        fn.table()
        input_1 = input("Do you want to 1. Order a meal 2. back to the main menu (1/2):")

        while not input_1 == "1" and not input_1 == "2":
                input_1 = input("Do you want to 1. Order a meal 2. back to the main menu (1/2):")

        if input_1 == "1":
            buy.input_4()
            break
        else:
            break