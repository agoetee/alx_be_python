"""
This program implements a division calculator that robustly handles errors 
like division by zero and non-numeric inputs using command line arguments
"""

def safe_divide(numerator, denominator):
    try:
        result = float(numerator) / float(denominator)
        return result
    
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."

    except ValueError:
       return "Error: Please enter numeric values only."