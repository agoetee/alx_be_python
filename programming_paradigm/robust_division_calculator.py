"""
This program implements a division calculator that robustly handles errors 
like division by zero and non-numeric inputs using command line arguments
"""

def safe_divide(numerator, denominator):
    try:
        result = float(numerator) / float(denominator)
        return result
    
    except ZeroDivisionError:
        return "Cannot divide by Zero"

    except ValueError:
       return "The value has to be a number"