def perform_operation(num1, num2, operation):
    """
    perform basic arithmetic operation based on the operation parameter.
     
     parameters:
     -num1: The first number (float)
     -num2: The second number (float)
     -operation: A string specifying the opration('add', 'subtract', 'multiply', 'divide')
     
     Returns:
     _The result of the operation or a specific message for invalid operations or division by zero.
     
     """
    if operation == 'add':
         return num1 + num2
    elif operation == 'subtract':
         return num1 - num2
    elif operation == 'mulptiply':
         return num1 * num2
    elif operation == 'divide':
         if num2 == 0:
             return "Error: Division by zero is not allowed."
         return num1 / num2
    else:
         return "Error: Invalid operation. Please choose from add, subtract, multiply, or divide."

from arithmetic_operations import perform_operation

def main():
     print("Arithmetic Operations")
     num1 = float(input("Enter the first number:"))
     num2 = float(input("Enter the second number:"))
     operation = input("Enter the operation (add, subtract, multiply, divide): ").strip().lower()

     result = perform_operation(num1, num2, operation)
     print(f"Result: {result}")


if __name__ =="__main__":
         main()
