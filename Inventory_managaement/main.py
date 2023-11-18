#importing other functions from different files
from buy_sellop import *
from operation import oprbill
from write import *
from read import *


print("\n                                 Welcome admin!!\n")

while True:
    #User interface after running the program
    print("-------------------------------------------------------------------------------")
    print("|                            RANDOM ELECTRONICS                                |")
    print("|                    Kamalpokhari, Kathmandu | 9849912300                      |")
    print("-------------------------------------------------------------------------------")
    print("|             1. Press 1 to check the stock                                    |")
    print("|             2. Press 2 if you want to Buy from manufacturer                  |")
    print("|             3. Press 3 if you want to Sell to customers                      |")
    print("|             4. Press 4 if you want to Exit from the system                   |")
    print("-------------------------------------------------------------------------------")
    try:            #exceptional handling
        imp_list = read_l()         #import the list of the laptops detail from the stock in a 2d list
        choice = int(input("\nWhat do you want to do? "))
        print("\n-------------------------------------------------------------------------------")

        if choice == 1:
            display_function(imp_list)          #calls the function that displays the 2d list of laptops details well formated in shell
        elif choice == 2:
            buy_list, new_data = buy_function(imp_list)                 #calls the function that stores the id and quantity of laptop and update the list with new quantity
            new_database(new_data)                                      #calls the function that writes the new list of laptop into the txt file
            bill_2dlist, amount = oprbill(buy_list, imp_list)           #calls the function that calculates the net amount, gross amount for the bill
            B_bill(bill_2dlist,amount)                                  #calls the function that prints the details of laptop in a bill in a txt file and omn the shell
        elif choice == 3:
            sell_list, new_data = sell_function(imp_list)               #calls the function that stores the id and quantity of laptop and update the list with new quantity
            new_database(new_data)                                      #calls the function that writes the new list of laptop into the txt file
            bill_2dlist, amount = oprbill(sell_list, imp_list)          #calls the function that calculates the net amount, gross amount for the bill
            S_bill(bill_2dlist,amount)                                  #calls the function that prints the details of laptop in a bill in a txt file and omn the shell
        elif choice == 4:       #program can only be exited if the user inputs 4
            print("\n                   **Thank you for your time**\n")
            break
        else:
            print("\nInvalid choice. Please enter 1, 2, 3 or 4\n")
    except:
        print("\n-------------------------------------------------------------------------------")
        print("\nPlease enter a number\n\n")


