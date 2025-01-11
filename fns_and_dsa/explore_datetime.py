import datetime

#Part 1: Display the current Date and Time
def display_current_datetime():
    """
    Display the current date and time in a readable format.
    """
    current_date = datetime.datetime.now()
    print(f"Current date and time: {current_date.strftime('%Y-%m-%d %H:%M:%S')}")

#Part 2: Calculate a Future Date 
def calculate_future_date(days_to_add):
    """
    Calculate and display the future date after adding the specified number of days.
    """
    current_date = datetime.datetime.now()
    future_date = current_date + datetime.timedelta(days=days_to_add)
    print(f"Future date: {future_date.strftime('%Y-%m-%d')}")
#Main function
def main():
    #Display the current date and time
    display_current_datetime()

    #Ask the user for the number of days to add
    days = int(input("Enter the number of days to add to the current date: "))
    
    #Calculate and display the future date
    calculate_future_date(days)

if __name__ == "__main__":
     main()

