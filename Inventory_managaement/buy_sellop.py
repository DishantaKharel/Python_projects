from read import display_function

def buy_function(data_list):

    display_function(data_list)         #calls a function that displays the laptops details
    
    length = len(data_list)
    loop = "y"
    first_list = []
    second_list = []

    while loop.lower() == "y":              #loops run until the user wants to buy more
        try:                                #exceptional handling
            choose = int(input("\nWhich product do you want to buy? "))         #asking user for the id of the laptop he wants

            if choose > 0 and choose <= length:                                 #checking if the id is there or not

                for i in range(choose):
                    new_list = data_list[i]
                    index = i                                                   #storing the id of the laptop

                while True:
                    try:
                        quantity = int(input("\nHow many do you want to buy? "))        #asking user for the number of items he wants to buy
                        break
                    except:
                        print("\nPlease enter a number.")

                confirm = input("\nDo you want to confirm your order? (Y/N): ")

                while True:

                    #this process adds the quantity to the quantity in the list if the order is confirmed
                    if confirm.lower() == "y" or confirm.lower() == "yes":

                        first_list.append(choose)
                        first_list.append(quantity)
                        second_list.append(first_list)
                        first_list = []

                        new_quantity = int(new_list[3]) + quantity      #adding the quantity given by the user with the prev quantity
                        new_list[3] = str(new_quantity)
                        data_list[index] = new_list

                        while True:
                            loop = input("\nDo you want to buy anything else? (Y/N):  ")

                            if loop.lower() == "y" or loop.lower() == "n":
                                break
                            else:
                                print("\nPlease try again!")

                        if loop.lower() == "y" or loop.lower() == "n":
                            print("\n-------------------------------------------------------------------------------")
                            break

                    elif confirm.lower() == "n" or confirm.lower() == "no":
                        print("\n-------------------------------------------------------------------------------")
                        break
                    else:
                        print("\nWrong input! Please try again")
                        print("\n-------------------------------------------------------------------------------")
                        break

            else:
                print("\nInvalid choice. Please enter S.N from above list")

        except:
            print("\nPlease enter a number.")

    """returns the list of id and quantity the users provide
        returns the new list with updated quantity
    """
    return second_list, data_list


def sell_function(data_list):

    length = len(data_list)         #checks how many varieties laptops are there in the stock
    total_quantity = 0
    loop = "y"
    first_list = []
    second_list = []
    
    display_function(data_list)         #calls the function that displays the laptops details in shell

    while loop.lower() == "y":
        try:
            choose = int(input("\nWhich product do you want to sell? "))

            if choose > 0 and choose <= length:         #if the laptops id is there then only it will proceed

                for i in range(choose):
                    new_list = data_list[i]
                    index = i                           #stores the id of the laptop

                while True:
                    try:
                        quantity = int(input("\nHow many do you want to sell? "))

                        if quantity <= int(new_list[3]):                #checks whether there is enough number of laptops the user wants to buy
                            break
                        else:
                            print("\nUnfortunately, we currently do not have that much in our stock")
                    except:
                        print("\nPlease enter a number.")

                confirm = input("\nDo you want to confirm your order? (Y/N): ")

                while True:
                    # this process adds the quantity to the quantity in the list if the order is confirmed
                    if confirm.lower() == "y" or confirm.lower() == "yes":

                        first_list.append(choose)
                        first_list.append(quantity)
                        second_list.append(first_list)
                        first_list = []

                        new_quantity = int(new_list[3]) - quantity      #subtracting the quantity given by the user with the prev quantity
                        new_list[3] = str(new_quantity)
                        data_list[index] = new_list

                        while True:
                            loop = input("\nDo you want to buy anything else? (Y/N): ")

                            if loop.lower() == "y" or loop.lower() == "n":
                                break
                            else:
                                print("\nPlease try again!")
                                break

                        if loop.lower() == "y" or loop.lower() == "n":
                            print("\n-------------------------------------------------------------------------------")
                            break

                    elif confirm.lower() == "n" or confirm.lower() == "no":
                        print("\n-------------------------------------------------------------------------------")
                        break
                    else:
                        print("\nWrong input! Please try again")
                        print("\n-------------------------------------------------------------------------------")
                        break

            else:
                print("\nInvalid choice. Please enter S.N from above list")
        except:
            print("\nPlease enter a number")

    """returns the list of id and quantity the users provide
            returns the new list with updated quantity
    """
    return second_list, data_list


