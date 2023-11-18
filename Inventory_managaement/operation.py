def oprbill(items_list, data_list):        #gets the value of id and quantity of laptop selected by user in a list and the list of all the laptops in another list as a parameter
    choose_2dlist = []
    gross_amt = 0

    #if one item is bought twice then this process will only add the quantity in the first time
    first = 0
    while first < len(items_list):
        second = first + 1
        while second < len(items_list):
            if items_list[first][0] == items_list[second][0]:
                items_list[first][1] += items_list[second][1]
                items_list.pop(second)
            else:
                second += 1
        first += 1

    """This process calculates the net amount,gross amount of the laptops bought/sold
         and keeps it in a 2d list and returns it
    """
    for each in items_list:
        choose_num = each[0] - 1
        choosed_list = data_list[choose_num]
            
        for i in range(3):
            choosed_list.pop()                          #removing processor and graphics card details from the list
                
        dollar_price = choosed_list[2]
        quantity = each[1]
        choosed_list.append(str(quantity))
        choosed_list[2],choosed_list[3] = choosed_list[3],choosed_list[2]       #swapping the position of price and quantity in the list
        price = dollar_price.replace('$','')
        int_price = int(price)
        net_amount = int_price * quantity
        dollar_netamt = "$" + str(net_amount)                                   #while adding the amount in the list it should be converted into string otherwise it will not be printed in thw txt file
        gross_amt += net_amount
        choosed_list.append(dollar_netamt)
        choose_2dlist.append(choosed_list)
        choosed_list = []

        #returning the list of choosen laptops and the gross amount
    return choose_2dlist, gross_amt