#Prompt the user for the size of the pattern
size = int(input("Enter the size of the pattern:"))
#Use a while loop to iterate through rows
row = 0
while row < size:
    #Use a for loop to print stars in each row
    for _ in range(size):
       print("*", end="")
    print()#Move to the next line after printing one row
    row += 1
