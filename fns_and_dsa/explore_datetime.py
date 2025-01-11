#import necessary components from the atetime module
from datetime import datetime, timedelta

#Function to display the current date and time
def display_current_datetime():
    
    current_date = datetime.now()
    print(f"Current date and time: {current_date.strftime('%Y-%m-%d %H:%M:%S')}")

#Function to calculate a future date 
def calculate_future_date():
    try:
        days_to_add = int(input("Enter the number of days to add to the current date:"))
        future_date = datetime.now() + timedelta(days=days_to_add)
        print(f"Future date: {future_date.strftime('%Y-%m-%d')}")
    except ValueError:
        print(f"Invalid input. Please enter an integer value for the number of days.")

#Main execution        

if __name__ == "__main__":
     display_current_datetime()
     calculate_future_date()

