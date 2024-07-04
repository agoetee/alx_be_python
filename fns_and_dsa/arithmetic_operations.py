"""
This script will define a function that performs basic arithmetic 
operations. This function, perform_operation, will be 
imported and used in a separate main.py script, which we provide.
"""

def perform_operation(num1: float, num2: float, operation: str):
    operation = ['add', 'subtract', 'multiply', 'divide']

    match operation:
        case 'add':
            result = num1 + num2
        case 'subtract':
            result = num1 - num2
        case 'multiply':
            result = num1 * num2
        case 'divide':
            if num2 == 0:
                print("Divisor cannot be 0")
            else:
                result = num1 / num2
        case _ :
            print("Invalid operation")
