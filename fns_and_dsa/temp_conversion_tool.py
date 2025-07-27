# ✅ Requirement 1: Define Global Conversion Factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5

# ✅ Requirement 2: Implement Conversion Functions
def convert_to_celsius(fahrenheit):
    """
    Converts Fahrenheit to Celsius using the global conversion factor.
    """
    # Using global variable (read-only access)
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    """
    Converts Celsius to Fahrenheit using the global conversion factor.
    """
    # Using global variable (read-only access)
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

# ✅ Requirement 3: User Interaction
def main():
    temp_input = input("Enter the temperature to convert: ").strip()
    unit_input = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

    # ✅ Requirement 4: Implementation of ValueError
    try:
        temperature = float(temp_input)
    except ValueError:
        raise ValueError("Invalid temperature. Please enter a numeric value.")

    if unit_input == 'F':
        converted = convert_to_celsius(temperature)
        print(f"{temperature}°F is {converted}°C")
    elif unit_input == 'C':
        converted = convert_to_fahrenheit(temperature)
        print(f"{temperature}°C is {converted}°F")
    else:
        raise ValueError("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")

# ✅ Entry point
if __name__ == "__main__":
    try:
        main()
    except ValueError as ve:
        print(ve)
