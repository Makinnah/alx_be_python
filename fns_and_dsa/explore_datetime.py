from datetime import datetime, timedelta

def display_current_datetime():
    current_date = datetime.now()  # ✅ Save current date
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")  # ✅ Format as “YYYY-MM-DD HH:MM:SS”
    print(f"Current date and time: {formatted_date}")

def calculate_future_date(days_to_add):
    current_date = datetime.now()
    future_date = current_date + timedelta(days=days_to_add)  # ✅ Save future date
    formatted_future = future_date.strftime("%Y-%m-%d")  # ✅ Format as “YYYY-MM-DD”
    print(f"Future date: {formatted_future}")

def main():
    display_current_datetime()

    try:
        days = int(input("Enter the number of days to add to the current date: "))
        calculate_future_date(days)
    except ValueError:
        print("Invalid input. Please enter an integer.")

if __name__ == "__main__":
    main()
