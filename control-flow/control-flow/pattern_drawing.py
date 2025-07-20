# Ask the user for the size of the pattern
size = int(input("Enter the size of the pattern: "))

# Use a while loop to handle rows
row = 0
while row < size:
    # Use a for loop to print asterisks in each row
    for col in range(size):
        print("*", end="")
    print()  # Move to the next line after each row
    row += 1
