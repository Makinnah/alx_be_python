# ✅ Definition of global conversion factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5

# ✅ Implement conversion functions
def convert_to_celsius(fahrenheit):
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

# ✅ User interaction
def main():
    temperature_input = input("Enter the temperature to convert: ")
    unit_input = input("Is this temperature in Celsius or Fahrenheit? (C/F): ")

    # ✅ Implementation of ValueError
    try:
        temperature = float(temperature_input)
    except:
        raise ValueError("Invalid temperature. Please enter a numeric value.")

    unit = unit_input.strip().upper()

    if unit == "F":
        result = convert_to_celsius(temperature)
        print(f"{temperature}°F is {result}°C")
    elif unit == "C":
        result = convert_to_fahrenheit(temperature)
        print(f"{temperature}°C is {result}°F")
    else:
        raise ValueError("Invalid temperature. Please enter a numeric value.")

if __name__ == "__main__":
    try:
        main()
    except ValueError as e:
        print(e)
