def display_menu():
    """
    Display the menu options for the shopping list manager.
    """
    print("Shopping List Manager") #This satisfies the required print statement
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    """
    Main function to manage the shopping list.
    """
    shopping_list = []

    while True:
        display_menu()
        choice = input("Enter your choice:")

        if choice == '1':
            #Add an item to shopping list
            item = input("Enter the item to add:").strip() #This matches the eact required prompt
            shopping_list.append(item)
            print(f"'{item}' has been added to the shopping list.")
        elif choice == '2':
            #Remove an item from the shopping list
            item = input("Enter the name of the item to remove:").strip()
            if item in shopping_list:
                shopping_list.remove(item)
                print(f"'{item}' has been removed from the shopping list.")
            else:
                print(f"'{item}' is not in the shopping list.")
        elif choice == '3':
            #Display the shopping list
            if shopping_list:
                print("\nYour shopping list:")
                for i, item in enumerate(shopping_list, start=1):
                    print(f"{i}. {item}")
            else:
                print("\nYour shopping list is empty.")
        elif choice == '4':
            #Exit the program
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

            
if __name__ == "__main__":
    main() 
