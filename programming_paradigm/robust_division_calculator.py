def safe_divide(numerator, denominator):
    """
    Safely divide two numbers with error handling for:
    - Non-numeric inputs
    - Division by zero
    """
    try:
        num = float(numerator)
        den = float(denominator)
    except ValueError:
        return "Error: Please enter numeric values only."

    try:
        result = num / den
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."

    return f"The result of the division is {result}"
