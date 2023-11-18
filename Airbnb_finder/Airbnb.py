import matplotlib.pyplot as plt
def read_csv(filename):
    data = []
    with open(filename, 'r') as fileobj:
        next(fileobj)
        for line in fileobj:
            fields = line.strip().split(',')
            data.append(fields)
    return data
def filter_by_price_range(data, min_price, max_price):
    return [row for row in data if min_price <= float(row[13]) <= max_price]

def filter_by_minimum_nights(data, min_nights):
    return [row for row in data if int(row[14]) >= min_nights]

def filter_by_cancellation_rate(data, max_cancellation_rate):
    return [row for row in data if float(row[18]) <= max_cancellation_rate]

def filter_by_bedrooms_count(data, bedrooms_count):
    return [row for row in data if int(row[9]) == bedrooms_count]

def filter_by_review_scores_rating_range(data, min_rating, max_rating):
    return [row for row in data if min_rating <= float(row[16]) <= max_rating]

def apply_filters():
    filename = 'Dataset.csv'
    data = read_csv(filename)

    # Applying filters
    filtered_data = data

    filter_criteria = input("Enter filters in the format (filter_name:value) separated by commas: ")
    print("\n")
    if filter_criteria:
        filters = filter_criteria.split(',')
        for f in filters:
            filter_name, value = f.split(':')
            if filter_name.upper() == 'PRICE':
                min_price, max_price = map(float, value.split('-'))
                filtered_data = filter_by_price_range(filtered_data, min_price, max_price)
            elif filter_name.upper() == 'MINIMUM_NIGHTS':
                min_nights = int(value)
                filtered_data = filter_by_minimum_nights(filtered_data, min_nights)
            elif filter_name.upper() == 'CANCELLATION_RATE':
                max_cancellation_rate = float(value)
                filtered_data = filter_by_cancellation_rate(filtered_data, max_cancellation_rate)
            elif filter_name.upper() == 'BEDROOMS_COUNT':
                bedrooms_count = int(value)
                filtered_data = filter_by_bedrooms_count(filtered_data, bedrooms_count)
            elif filter_name.upper() == 'REVIEW_SCORES_RATING':
                min_rating, max_rating = map(float, value.split('-'))
                filtered_data = filter_by_review_scores_rating_range(filtered_data, min_rating, max_rating)
            else:
                print(f"Unknown filter '{filter_name}'")

    return filtered_data
def display_data_as_output(filtered_data):
    print(f"S.N  {'Host_Response_Rate':<20} {'Host_Identity_Verified':<24} {'Host_Total_Listings_Count':<27} {'Unique_City_ID':<16} {'Location_Verified ':<19} {'Property_Type':<14} {'Room_Type':<12} {'Max_Accomodation ':<16} {'Bathrooms_Count ':<14} {'Bedrooms_Count ':<14} {'Beds_Count':<14} {'Bed_Type':<14} {'Amenities_Price ':<18} {'Price':<11} {'Minimum_Nights':<17} {'Number_of_Reviews':<18} {'Review_Scores_Rating':<24} {'Instant_Bookable':<18} {'Cancellation_Rate':<19} {'Reviews_per_Month':<19} {'Fraud_Count':<19}  ")
    for sn_num, data in enumerate(filtered_data):
        sn = str(sn_num + 1).rjust(2, ' ')
        Host_Response_Rate = data[0].ljust(28)
        Host_Identity_Verified = data[1].ljust(28)
        Host_Total_Listings_Count = data[2].ljust(21)
        Unique_City_ID = data[3].ljust(18)
        Location_Verified = data[4].ljust(18)
        Property_Type = data[5].ljust(12)
        Room_Type = data[6].ljust(16)
        Max_Accomodation = data[7].ljust(14)
        Bathrooms_Count = data[8].ljust(16)
        Bedrooms_Count = data[9].ljust(14)
        Beds_Count = data[10].ljust(14)
        Bed_Type = data[11].ljust(14)
        Amenities_Price = data[12].ljust(14)
        Price = data[13].ljust(16)
        Minimum_Nights = data[14].ljust(19)
        Number_of_Reviews = data[15].ljust(17)
        Review_Scores_Rating = data[16].ljust(24)
        Instant_Bookable = data[17].ljust(19)
        Cancellation_Rate = data[18].ljust(19)
        Reviews_per_Month = data[19].ljust(14)
        Fraud_Count = data[20].ljust(14)
        print(f"{sn}.  {Host_Response_Rate} {Host_Identity_Verified} {Host_Total_Listings_Count} {Unique_City_ID} {Location_Verified} {Property_Type} {Room_Type} {Max_Accomodation} {Bathrooms_Count} {Bedrooms_Count} {Beds_Count} {Bed_Type} {Amenities_Price} {Price} {Minimum_Nights} {Number_of_Reviews} {Review_Scores_Rating} {Instant_Bookable} {Cancellation_Rate} {Reviews_per_Month} {Fraud_Count}")
    print("\n")


def calculate_average(data, x_index, y_index):
    averages = {}

    for entry in data:
        x_value = entry[x_index]
        y_value = int(entry[y_index])  # Convert y_value to int

        if x_value not in averages:
            averages[x_value] = []

        averages[x_value].append(y_value)

    x_values = []
    y_values = []

    for x_value, y_values_list in averages.items():
        x_values.append(x_value)
        y_values.append(sum(y_values_list) / len(y_values_list))

    return x_values, y_values
def display_data_as_graph(filtered_data):
    while True:
        print("""\n1. Price \n2. Bedrooms count\n3. Property type\n4. Review scores rating \n""")
        x_column = int(input("Enter the S.N of which you want to display in x-axis: "))

        if x_column == 1:
            x_index = 13
            x_axis = "Price"
            break

        elif x_column == 2:
            x_index = 9
            x_axis = "Bedrooms count"
            break

        elif x_column == 3:
            x_index = 5
            x_axis = "Property type"
            break

        elif x_column == 4:
            x_index = 16
            x_axis = "Review scores rating"
            break

        else:
            print("Invalid input please try again\n")

    while True:
        print("""\n1. Price\n2. Cancellation rate\n3. Amenities_price\n""")
        y_column = int(input("Enter the S.N of which you want to display in y-axis: "))

        if y_column == 1:
            y_index = 13
            y_axis = "Price"
            break

        elif y_column == 2:
            y_index = 18
            y_axis = "Cancellation rate"
            break

        elif y_column == 3:
            y_index = 12
            y_axis = "Amenities_price"
            break

        else:
            print("Invalid input please try again\n")
    type = int(input("""\n1. Histogram\n2. Scatter plots\n\nEnter the S.N of the type of bar you want to use: """))
    x_values = [entry[x_index] for entry in filtered_data]
    y_values = [entry[y_index] for entry in filtered_data]

    x_values, y_values = calculate_average(filtered_data, x_index, y_index)
    y_values = [int(val) for val in y_values]
    plt.ylim(0, max(y_values) + 300)

    if type == 1:
        plt.bar(x_values, y_values, width=0.4)
        plt.xlabel(x_axis)
        plt.ylabel(y_axis)
        plt.title("Airbnb Data")
        plt.show()

    elif type == 2:
        plt.scatter(x_values, y_values)
        plt.xlabel(x_axis)
        plt.ylabel(y_axis)
        plt.title("Airbnb Data")
        plt.show()

    else:
        print("Invalid input please try again\n")

def main():
    filename = "Dataset.csv"
    data = read_csv(filename)
    filters = {}

    while True:
        print("\n--- Menu ---")
        print("1. Apply Filter")
        print("2. Display Data as Output")
        print("3. Display Data as Graph")
        print("4. Reset Filters")
        print("5. Exit")
        print("\n")
        
        choice = input("Enter your choice (1/2/3/4/5): ")
        print("\n")

        if choice == '1':
            filtered_data = apply_filters()
            print("Filter applied successfully.")

        elif choice == '2':
            display_data_as_output(filtered_data)

        elif choice == '3':
            display_data_as_graph(filtered_data)

        elif choice == '4':
            filtered_data = {}
            print("Filters reset successfully.")

        elif choice == '5':
            print("\n")
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()

