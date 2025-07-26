# fns_and_dsa/arithmetic_operations.py

def perform_operation(num1: float, num2: float, operation: str) -> float | str:
    """
    Perform basic arithmetic operations.

    Parameters:
    - num1 (float): First number
    - num2 (float): Second number
    - operation (str): One of 'add', 'subtract', 'multiply', 'divide'

    Returns:
    - float: Result of the operation
    - str: Error message if operation is invalid or division by zero
    """
    match operation:
        case 'add':
            return num1 + num2
        case 'subtract':
            return num1 - num2
        case 'multiply':
            return num1 * num2
        case 'divide':
            if num2 == 0:
                return "Error: Division by zero"
            return num1 / num2
        case _:
            return "Error: Invalid operation"
