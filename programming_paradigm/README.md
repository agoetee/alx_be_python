# Concept about OOP, Exception Handling and Unittesting

## 0. Create a Simple Bank Account Class 
__Objective__: Understand the fundamentals of OOP in Python by implementing a `BankAccount` class that encapsulates banking operations. Use command line arguments to interact with instances of this class.
__Task Description__:

You will create two Python scripts: `bank_account.py`, which contains the `BankAccount` class, and `main-0.py`, which interfaces with the class through command line arguments to perform banking operations.
`bank_account.py`:

 1. __Class Definition__:
        - Define a class named `BankAccount`.
        - Use the `__init__` method to initialize an `account_balance` attribute. Optionally, accept an initial balance parameter, defaulting to zero.

 2. __Encapsulation and Behaviors__:
        - Implement `deposit(amount)`, `withdraw(amount)`, and `display_balance()` methods.
        - `deposit` should add the specified amount to `account_balance`.
        - `withdraw` should deduct the amount from `account_balance` if funds are sufficient, returning `True`; otherwise, return `False` and do not alter the balance.
        - `display_balance` should print the current balance in a user-friendly format.

`main-0.py` for Command Line Interaction:

This script utilizes `BankAccount` through command line arguments for banking operations.

```py
import sys
from bank_account import BankAccount

def main():
    account = BankAccount(100)  # Example starting balance
    if len(sys.argv) < 2:
        print("Usage: python main.py <command>:<amount>")
        print("Commands: deposit, withdraw, display")
        sys.exit(1)

    command, *params = sys.argv[1].split(':')
    amount = float(params[0]) if params else None

    if command == "deposit" and amount is not None:
        account.deposit(amount)
        print(f"Deposited: ${amount}")
    elif command == "withdraw" and amount is not None:
        if account.withdraw(amount):
            print(f"Withdrew: ${amount}")
        else:
            print("Insufficient funds.")
    elif command == "display":
        account.display_balance()
    else:
        print("Invalid command.")

if __name__ == "__main__":
    main()
```
__Sample Command Line Usage and Expected Outputs:__

 - __Deposit:__

```shell
   python main-0.py deposit:50
```

Expected Output: `Deposited: $50`

- __Withdraw with Sufficient Funds:__

```sh
python main-0.py withdraw:20
```

Expected Output: `Withdrew: $20`

 - __Withdraw with Insufficient Funds:__

```sh
python main-0.py withdraw:150
```

Expected Output: `Insufficient funds`.

 - __Display Balance__:

```sh
python main-0.py display
```

Expected Output: `Current Balance: $[amount]`

__Implementation Notes for you:__

 - Ensure your BankAccount class in `bank_account.py` correctly implements the specified functionalities and adheres to the principles of encapsulation.
 - Use `main.py` to test your `BankAccount` class by performing various operations. Adjust the initial balance as needed for testing different scenarios.
 - This task combines learning OOP concepts with practical command line interaction, enhancing your understanding of Python programming.


## 1. Robust Division Calculator with Command Line Arguments 
__Objective:__ Implement a division calculator that robustly handles errors like division by zero and non-numeric inputs using command line arguments.
__Task Description:__

Create two Python scripts: `robust_division_calculator.py`, which contains the division logic including error handling, and `main.py`, which interfaces with the user through the command line.
``__robust_division_calculator.py__``:

Define a function `safe_divide(numerator, denominator)` that performs division, handling potential errors:

 - Division by Zero: Use a try-except block to catch `ZeroDivisionError`.
 - Non-numeric Input: Attempt to convert arguments to floats. Use a try-except block to catch `ValueError` for non-numeric inputs.
 - Return appropriate messages for errors or the result for successful division.

`main.py` for Command Line Interaction:

This script will import `safe_divide` from `robust_division_calculator.py` and use it to divide numbers provided as command line arguments.

```py
import sys
from robust_division_calculator import safe_divide

def main():
    if len(sys.argv) != 3:
        print("Usage: python main.py <numerator> <denominator>")
        sys.exit(1)

    numerator = sys.argv[1]
    denominator = sys.argv[2]

    result = safe_divide(numerator, denominator)
    print(result)

if __name__ == "__main__":
    main()
```

__Expected Behavior:__

The script is executed from the command line with two additional arguments representing the numerator and denominator. Here are sample commands and the expected outputs:

 - __Normal Division__:

  ```sh
  python main.py 10 5
  ```

Expected Output: `The result of the division is 2.0`

 - __Division by Zero:__

  ```s
  python main.py 10 0
  ```

Expected Output: `Error: Cannot divide by zero`.

 - __Invalid Input (Non-numeric)__:

  ```sh
  python main.py ten 5
  ```

Expected Output: `Error: Please enter numeric values only`.

__Implementation Notes for you:__

 - Focus on error handling within safe_divide in robust_division_calculator.py. Ensure you cover the scenarios detailed above.
 - Test your function using main.py by passing different types of inputs via command line arguments. This method allows you to quickly assess how well your error handling works in various situations.
 - This task helps you practice writing error-resistant code, a crucial skill in software development.
