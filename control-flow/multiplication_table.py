#Prompt user to input a number
number = int(input("Enter a number to see its multiplication table:"))
#Generate the multiplication table using for loop
for i in range(1, 11): #Loop throught numbers 1 to 10
    product = number * i #Calculate the product
    print(f"{number} * {i} = {product}") #Print the result

