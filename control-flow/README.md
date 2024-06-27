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

## 2. Multiplication Table Generator 
Objective: Use a for loop to generate and print the multiplication table for a given number.

Task Description:

Create a Python script named multiplication_table.py. This script will ask the user to enter a number, then use a for loop to print the multiplication table for that number from 1 to 10.

Instructions:

    Prompt User for a Number:
        Ask the user to input a number for which they want to see the multiplication table: Enter a number to see its multiplication table:.
        Save it in a variable name number

    Generate and Print the Multiplication Table:
        Use a for loop to iterate through the numbers 1 to 10.
        For each iteration, calculate the product of the user’s number and the iterator (the current number in the loop from 1 to 10).
        Print each line of the multiplication table in the format: “X * Y = Z”, where X is the user’s number, Y is the current number in the loop, and Z is the product.

Example Interaction:

If the user inputs 5, the output should be:

Enter a number to see its multiplication table: 5
5 * 1 = 5
5 * 2 = 10
5 * 3 = 15
5 * 4 = 20
5 * 5 = 25
5 * 6 = 30
5 * 7 = 35
5 * 8 = 40
5 * 9 = 45
5 * 10 = 50



