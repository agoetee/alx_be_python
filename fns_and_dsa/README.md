## The description of the `fns_and_dsa` directory

# Tasks

## 0. Arithmetic Operations Function

Create a Python script named `arithmetic_operations.py`. In this script, define a function that performs basic arithmetic operations. This function, `perform_operation`, will be imported and used in a separate `main.py` script, which we provide.
Requirements for `arithmetic_operations.py`:

 - __Function Definition__:
        Define a function named `perform_operation`.
        Parameters: `num1` (float), `num2` (float), and `operation` (string). The `operation` parameter accepts four possible values: '`add`', '`subtract`', '`multiply`', or '`divide`'.
        The function should execute the arithmetic operation based on the `operation` parameter and the numerical values provided.
        For division, include handling for division by zero, returning a specific message or value that your `main.py` script can recognize and display appropriately.
        Return the result of the arithmetic operation.

Provided `main.py` for Testing:

```
from arithmetic_operations import perform_operation

def main():
    print("Arithmetic Operations")
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    operation = input("Enter the operation (add, subtract, multiply, divide): ").strip().lower()

    result = perform_operation(num1, num2, operation)
    print(f"Result: {result}")

if __name__ == "__main__":
    main()
```

Here is an example output

```
>>> python .\main.py
Arithmetic Operations
Enter the first number: 5
Enter the second number: 6
Enter the operation (add, subtract, multiply, divide): add
Result: 11.0
```

**Note**: - Focus on implementing the `perform_operation` function in `arithmetic_operations.py`. Ensure your function correctly handles the operations based on the inputs. - You do not need to create or modify `main.py`. It is provided for you to test your function. The checker will use this `main.py` to import your `arithmetic_operations.py` script and test its functionality.


## 1. Shopping List Manager
__Objective__: Utilize Python lists to create a simple shopping list manager that allows users to add items, view the current list, and remove items.

__Task Description__:

Create a Python script named `shopping_list_manager.py` that implements a simple interface for managing a shopping list. This task focuses on using lists to store and manipulate data dynamically.

__Requirements__:

    1. **Core Functionality**:
        - Your script should start with an empty list named shopping_list.
        - Implement functionality to add items to the list, remove items, and display the current list.

    2. __User Interface__:
        - Use a loop to continuously display a menu with options to the user until they choose to exit. The menu should offer options to add an item, remove an item, view the list, and exit.
        - For adding items, prompt the user for the item name and append it to `shopping_list`.
        - For removing items, ask the user for the item name and remove it from `shopping_list`. If the item is not found, display a message indicating so.
        - To view the list, print each item in `shopping_list` to the console.
        - Ensure your script handles invalid menu choices gracefully.

`shopping_list_manager.py` Skeleton:

```
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
            # Prompt for and add an item
            pass
        elif choice == '2':
            # Prompt for and remove an item
            pass
        elif choice == '3':
            # Display the shopping list
            pass
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
    
```

__Note for Students__:

    - You are responsible for completing the `main()` function with the appropriate logic to handle adding, removing, and displaying items in the `shopping_list`.
    - This task introduces you to working with lists in a practical scenario, enhancing your understanding of how dynamic data structures can be manipulated and utilized in Python programs.

