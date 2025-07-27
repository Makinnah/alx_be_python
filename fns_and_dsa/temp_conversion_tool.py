# ✅ Requirement: Define Global Conversion Factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9  # Used to convert F to C
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5  # Used to convert C to F

# ✅ Requirement: Implement Conversion Functions
def convert_to_celsius(fahrenheit):
    """
    Converts Fahrenheit to Celsius using the global conversion factor.
    """
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    """
    Converts Celsius to Fahrenheit using the global conversion factor.
    """
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

# ✅ Requirement: User Interaction + Input Validation
def main():
    try:
        # Prompt user for temperature input
        temp_input = input("Enter the temperature to convert: ").strip()

        # ✅ Requirement: Implementation of ValueError for non-numeric input
        temp_value = float(temp_input)  # Raises ValueError if input is not numeric

        # Prompt user for unit type
        unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

        # ✅ Requirement: Call appropriate conversion function based on unit
        if unit == 'F':
            converted = convert_to_celsius(temp_value)
            print(f"{temp_value}°F is {converted}°C")
        elif unit == 'C':
            converted = convert_to_fahrenheit(temp_value)
            print(f"{temp_value}°C is {converted}°F")
        else:
            # ✅ Requirement: Raise error for invalid unit input
            raise ValueError("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")

    except ValueError:
        # ✅ Requirement: Handle invalid temperature input
        print("Invalid temperature. Please enter a numeric value.")

# ✅ Requirement: Script entry point
if __name__ == "__main__":
    main()
