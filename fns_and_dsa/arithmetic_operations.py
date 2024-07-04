"""
This script will define a function that performs basic arithmetic 
operations. This function, perform_operation, will be 
imported and used in a separate main.py script, which we provide.
"""

def perform_operation(num1, num2, operation):
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
                return "Divisor cannot be 0"
            elif num2 != 0:
                result = num1 / num2
        case _ :
            return "Invalid operation"
