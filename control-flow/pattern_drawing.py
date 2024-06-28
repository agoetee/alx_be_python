# This file uses nested loops to draw a simple text based pattern

size = int(input("Enter the size of the pattern: "))
initial = 1

while initial <= size:
    for i in range(1, size + 1):
        print("*", end="")
    print()
    initial += 1
