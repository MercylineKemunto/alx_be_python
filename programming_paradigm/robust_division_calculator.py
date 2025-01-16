def safe_divide(numerator, denominator):
    try:
        #Convert input values to floats
        numerator = float(numerator)
        denominator = float(denominator)
    except ValueError:
        #Handle non-numeric inputs
        return "Error: Please enter numeric values only."
    try:
        #Perform division
        result = numerator / denominator
        return f"The result of the division is {result:.2f}"
    except ZeroDivisionError:
        #Handle division by zero
        return "Error: Cannot divide by zero."

