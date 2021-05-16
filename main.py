import pymongo
import sys
import manage_db
import options


def main():
    print("Welcome")
    isQuit = False
    while (not isQuit):
        options.print_menu()
        option = input("Your choice: ").lower()
        if option == "q":
            print("Goodbye!")
            break
        elif option == "o":
            manage_db.clear_db()
            manage_db.add_data_to_db()

        elif option == "1":
            options.find_beverage()
        elif option == "2":
            options.cal_income()
        elif option == "3":
            options.create_bill()
        elif option == "4":
            options.cal_net_worth()
        elif option == "5":
            options.update_beverage()
        else:
            print("invalid option!!!")
        print("\n"*3)


if __name__ == "__main__": 
    main()
    sys.exit(0)

