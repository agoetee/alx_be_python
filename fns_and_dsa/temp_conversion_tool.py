"""
"""

FAHRENHEIT_TO_CELSIUS_FACTOR = (5 / 9)
CELSIUS_TO_FAHRENHEIT_FACTOR = (9 / 5)


#function to convert from farenheit to celsius
def convert_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    return celsius

#function to convert from celcius to farenheit
def convert_to_fahrenheit(celsius):
    farenheit = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
    return farenheit

def main():
    temperature = float(input("Enter the temperature to convert: "))
    unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").lower()
    match unit:
        case 'c':
            converted = convert_to_fahrenheit(temperature)
            print(f"{temperature}°F is {converted}°C")

        case 'f':
            converted = convert_to_celsius(temperature)
            print(f"{temperature}°C is {converted}°F")
        case _:
            print("Invalid input")

if __name__ == '__main__':
    main()
