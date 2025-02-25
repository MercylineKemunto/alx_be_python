#Global Conversion Factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

#Function to convert Fahrenheit to Celsius
def convert_to_celsius(fahrenheit):
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

#Function to convert Celsius to Fahrenheit
def convert_to_fahrenheit(celsius):
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

#Main execution
if __name__ == "__main__":
    try:
        #Prompt the user for temperature input
        temperature = float(input("Enter the temperature to convert:"))
        unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

        #Determine the conversion based on user input
        if unit == "F":
            convert_temp = convert_to_celsius(temperature)
            print(f"{temperature}°F is {convert_temp:.2f}°C") 
        elif unit == "C":
            converted_temp = convert_to_fahrenheit(temperature)
            print(f"{temperature}°C is {converted_temp:.2f}°F")
        else:
            raise ValueError("Invalid temperature unit. Please enter 'C' or 'F' .") 
    except ValueError as e:
            print("Invalid temperature. Please enter a numeric value.")
