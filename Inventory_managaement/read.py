def read_l():
    data_list = []
    with open("database.txt","r") as files:         #read the file with the laptops details

        for line in files:
            individual_list = line.split(",")       #seperate the elements after every coma
            individual_list.pop()                   #removing unwanted data
            data_list.append(individual_list)

        #returns the data_list which contains the details of the laptops
        return data_list


def display_function(data_list):

    #this process is used to display the list of items in the shell in a well formated way
    print("\n")
    print(f"S.N  {'COMPANY':<16} {'PRODUCT':<18} {'PRICE':<10} {'Quantity':<10} {'PROCESSOR':<14} {'GRAPHICS CARD':<14}")
    for sn_num, data in enumerate(data_list):
        sn = str(sn_num+1).rjust(2, ' ')
        company = data[0].ljust(15)
        product = data[1].ljust(18)
        price = data[2].ljust(12)
        quantity = data[3].ljust(8)
        processor = data[4].ljust(14)
        graphics_card = data[5].ljust(14)
        print(f"{sn}.  {company} {product} {price} {quantity} {processor} {graphics_card}")
    print("\n")