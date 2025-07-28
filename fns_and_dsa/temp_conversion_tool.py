# ✅ Requirement: Define Global Conversion Factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5

# ✅ Requirement: Implement Conversion Functions
def convert_to_celsius(fahrenheit):
    """
    Convert Fahrenheit to Celsius using the global conversion factor.
    """
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    """
    Convert Celsius to Fahrenheit using the global conversion factor.
    """
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

# ✅ Requirement: User Interaction
def main():
    temp_input = input("Enter the temperature to convert: ").strip()
    unit_input = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

    # ✅ Requirement: Implementation of Value Error
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
        raise ValueError("Invalid temperature. Please enter a numeric value.")

# ✅ Requirement: Entry Point
if __name__ == "__main__":
    try:
        main()
    except ValueError as ve:
        print(ve)
