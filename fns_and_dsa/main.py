# fns_and_dsa/main.py

from arithmetic_operations import perform_operation

def main():
    print("Welcome to the Arithmetic Operations Program!")
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        operation = input("Choose operation (add, subtract, multiply, divide): ").strip().lower()

        result = perform_operation(num1, num2, operation)
        print(f"Result: {result}")
    except ValueError:
        print("Error: Please enter valid numbers.")

if __name__ == "__main__":
    main()
