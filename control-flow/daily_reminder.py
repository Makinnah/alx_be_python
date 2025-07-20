# Ask the user for task details
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Use match case to respond based on priority
match priority:
    case "high":
        message = f"Reminder: '{task}' is a high priority task"
    case "medium":
        message = f"Note: '{task}' is a medium priority task"
    case "low":
        message = f"Note: '{task}' is a low priority task"
    case _:
        message = f"'{task}' has an unknown priority level"

# Add time sensitivity if applicable
if time_bound == "yes":
    message += " that requires immediate attention today!"
else:
    message += ". Consider completing it when you have free time."

# Print the final reminder
print(message)
Enter your task: Submit assignment
Priority (high/medium/low): high
Is it time-bound? (yes/no): yes

Reminder: 'Submit assignment' is a high priority task that requires immediate attention today!
Enter your task: Organize bookshelf
Priority (high/medium/low): low
Is it time-bound? (yes/no): no

Note: 'Organize bookshelf' is a low priority task. Consider completing it when you have free time.
