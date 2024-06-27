# This tasks:

## 0. Weather Recommendation Program
__Objective__: Utilize conditional statements to guide program execution based on user input regarding weather conditions.

__Task Description__:

Create a Python script named weather_advice.py. This script will ask the user about the current weather conditions and provide clothing recommendations based on the input. This task aims to demonstrate the use of if, elif, and else statements to make decisions in a program.

__Instructions__:

 - Prompt User for Weather Input:
	- Ask the user to input the current weather from a predefined set of conditions: sunny, rainy, or cold.
	- Use the prompt: What's the weather like today? (sunny/rainy/cold):.

 - Provide Clothing Recommendations:
        Based on the user’s input, your program will recommend different types of clothing:
	- If the weather is “sunny”, recommend: Wear a t-shirt and sunglasses.
	- If the weather is “rainy”, recommend: Don't forget your umbrella and a raincoat.
	- If the weather is “cold”, recommend: Make sure to wear a warm coat and a scarf.
        Include an else statement that handles unexpected input by printing: Sorry, I don't have recommendations for this weather.

  - Output the Recommendation:
        Print the clothing recommendation based on the weather condition provided by the user.

Example Interaction:

What's the weather like today? (sunny/rainy/cold): sunny
Wear a t-shirt and sunglasses.

Or, for an unexpected input scenario:

What's the weather like today? (sunny/rainy/cold): windy
Sorry, I don't have recommendations for this weather.

## 1. Simple Calculator with Match Case 
**Objective**: Learn to use Match Case statements for handling multiple operations in a simple calculator program.

**Task Description**:

Develop a Python script named match_case_calculator.py. This calculator will prompt the user to enter two numbers and select an operation (addition, subtraction, multiplication, or division). The script will then perform the selected operation using a Match Case statement and display the result.

**Instructions**:

    - Prompt for User Input:
        - Ask the user to input two numbers (one at a time) using: Enter the first number: and  Enter the second number:
        - Make sure you use num1 and num2 for first and second numbers
        - Ask for the type of operation they’d like to perform: Choose the operation (+, -, *, /):.

    - Perform the Calculation Using Match Case:
        - Implement a Match Case statement that executes the chosen operation based on the user’s input.
            - For addition (+), subtract (-), multiply (*), and divide (/).
        - Ensure to handle the division by zero case gracefully, displaying a message if the user tries to divide by zero.

    - Output the Result:
        Display the result of the operation in a user-friendly message, e.g., The result is [result].

Example Interaction:

Enter the first number: 10
Enter the second number: 5
Choose the operation (+, -, *, /): *
The result is 50.


