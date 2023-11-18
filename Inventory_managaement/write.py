def new_database(data_list):  

    with open("database.txt", "w") as new_file:         #re-writing the file with the update quantity

        for each_line in data_list:
            listTostring = ','.join(each_line)          #joins the lines with a coma
            new_file.write(listTostring + ",\n")        #prints it in the file


def B_bill(choose_2dlist, gross_amt):
    import datetime                                     #importing real time date and time
    now = datetime.datetime.now()
    current_time = now.strftime("%Y_%m_%d_%H_%M_%S")
    current_timeanddate = now.strftime("%Y-%m-%d %H:%M:%S")
    customer = input("\nPlease enter the name of distributer : ")       #name of the distributer
    print("\n                   **THANK YOU FOR YOUR TIME**\n")
    print("*********************************************************************************\n\n")

    vat = 0.13
    total_amt = "$" + str(gross_amt)            #makes the gross amount into a string with a dollar
    vated_amt = gross_amt *(1+ vat)             #calculates the total amount with the vat
    dollar_vatamt = "$" + str(vated_amt)
        
    with open(f"{customer}_{current_time}.txt", 'w') as file:           #creates a file with unique name each time and prints the bill in it
        #details about the customer and the company
        file.write("                    RANDOM ELECTRONICS BILL")
        file.write("\n-----------------------------------------------------------------------\n")
        file.write("\nDISTRIBUTER: " + customer.upper())
        file.write("\n\nBILL DATE: " + current_timeanddate)
        file.write("\n\n-----------------------------------------------------------------------")
        file.write("\n\n-----------------------------------------------------------------------\n\n")
        file.write(f"S.N  {'COMPANY':<14} {'PRODUCT':<17} {'Quantity':<13} {'PRICE':<10} {'NET AMOUNT':<10}")
        file.write("\n\n")
        #this process generates the bill in the txt file in managed way
        for sn_num, data in enumerate(choose_2dlist):
            sn = str(sn_num+1).rjust(2, ' ')
            company = data[0].ljust(13)
            product = data[1].ljust(18)
            quantity = data[2].ljust(12)
            price = data[3].ljust(12)
            net_amount = data[4].ljust(18)
            file.write(f"{sn}.  {company} {product} {quantity} {price} {net_amount}")
            file.write("\n\n")
        file.write("-----------------------------------------------------------------------\n\n")
        file.write("Total amount:\t\t\t\t\t\t\t\t" + total_amt)
        file.write("\nVat:\t\t\t\t\t\t\t\t\t\t13%")
        file.write("\nGross amount:\t\t\t\t\t\t\t\t" + dollar_vatamt)
        file.write("\n\n-----------------------------------------------------------------------")
        file.write("\n\n\n                  **THANK YOU FOR SHOPPING**\n\n")

    with open(f"{customer}_{current_time}.txt", 'r') as show:           #reads the bill created and display the information in the shell
        print(show.read()) 


def S_bill(choose_2dlist, gross_amt):
    import datetime                                     #importing real time date and time
    now = datetime.datetime.now()
    current_time = now.strftime("%Y_%m_%d_%H_%M_%S")
    current_timeanddate = now.strftime("%Y-%m-%d %H:%M:%S")
    customer = input("\nPlease enter the name of customer : ")
    ph_num = input("\nPlease enter your phone number: ")
    address = input("\nPlease enter your address: ")
    print("\n                   **THANK YOU FOR YOUR TIME " + customer.upper() +"**\n")
    print("*********************************************************************************\n\n")

    shipping = 10
    total_amt = "$" + str(gross_amt)            #converts the gross amount into string
    shipped_amt = gross_amt + shipping          #calculates the total amount with the shipping cost
    dollar_vatamt = "$" + str(shipped_amt)
        
    with open(f"{customer}_{current_time}.txt", 'w') as file:       #creates a file with unique name each time and prints the bill in it
        # details about the customer and the company
        file.write("                          RANDOM ELECTRONICS")
        file.write("\n-----------------------------------------------------------------------\n")
        file.write("\nCUSTOMER: " + customer.upper())
        file.write("\n\nBILL DATE: " + current_timeanddate)
        file.write("\n\nPHONE NUMBER: " + ph_num)
        file.write("\n\nADDRESS: " + address)
        file.write("\n\n-----------------------------------------------------------------------")
        file.write("\n\n-----------------------------------------------------------------------\n\n")
        file.write(f"S.N  {'COMPANY':<14} {'PRODUCT':<17} {'Quantity':<13} {'PRICE':<10} {'NET AMOUNT':<10}")
        file.write("\n\n")

        # this process generates the bill in the txt file in managed way
        for sn_num, data in enumerate(choose_2dlist):
            sn = str(sn_num+1).rjust(2, ' ')
            company = data[0].ljust(13)
            product = data[1].ljust(18)
            quantity = data[2].ljust(12)
            price = data[3].ljust(12)
            net_amount = data[4].ljust(18)
            file.write(f"{sn}.  {company} {product} {quantity} {price} {net_amount}")
            file.write("\n\n")
        file.write("-----------------------------------------------------------------------\n\n")
        file.write("Total amount:\t\t\t\t\t\t\t\t" + total_amt)
        file.write("\nShipping cost:\t\t\t\t\t\t\t\t$10")
        file.write("\nGross amount:\t\t\t\t\t\t\t\t" + dollar_vatamt)
        file.write("\n\n-----------------------------------------------------------------------")
        file.write("\n\n\n                  **THANK YOU FOR SHOPPING**\n\n")

    with open(f"{customer}_{current_time}.txt", 'r') as show:               #reads the bill created and display the information in the shell
        print(show.read())
