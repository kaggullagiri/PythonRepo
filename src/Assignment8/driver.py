from src.Assignment8.util import printingpattern

# Taking the user input for the thickness
thickness = int(input("Enter thickness (Enter an odd number): "))

# Calling the utility function to generate and print the pattern
result = printingpattern(thickness)
for i in result:
    print(i)

