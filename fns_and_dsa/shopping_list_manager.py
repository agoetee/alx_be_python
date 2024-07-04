"""
 Utilize Python lists to create a simple shopping list manager that allows 
 users to add items, view the current list, and remove items.
"""

def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            item = input("Enter your item: ")
            shopping_list.append(item)        
        elif choice == '2':
            # Prompt for and remove an item
            item = input("Enter item to delete: ")

            for i in shopping_list:
                if item in shopping_list:
                    shopping_list.remove(item)
                    print(f"{item} removed successfully")
                else:
                    print(f"{item} not found")                
        elif choice == '3':
            for i in range(len(shopping_list)):
                print(shopping_list[i])
            # Display the shopping list
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()