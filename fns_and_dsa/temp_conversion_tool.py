# ✅ Requirement: Define Global Conversion Factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5

# ✅ Requirement: Implement Conversion Functions
def convert_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius using global conversion factor."""
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit using global conversion factor."""
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

# ✅ Requirement: User Interaction
def main():
    temp_str = input("Enter the temperature to convert: ").strip()
    unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

    # ✅ Requirement: Implementation of Value Error
    if not temp_str.replace('.', '', 1).isdigit() and not (temp_str.startswith('-') and temp_str[1:].replace('.', '', 1).isdigit()):
        raise ValueError("Invalid temperature. Please enter a numeric value.")

    temperature = float(temp_str)

    if unit == 'F':
        result = convert_to_celsius(temperature)
        print(f"{temperature}°F is {result}°C")
    elif unit == 'C':
        result = convert_to_fahrenheit(temperature)
        print(f"{temperature}°C is {result}°F")
    else:
        raise ValueError("Invalid temperature. Please enter a numeric value.")

# ✅ Requirement: Entry Point
if __name__ == "__main__":
    try:
        main()
    except ValueError as e:
        print(e)
