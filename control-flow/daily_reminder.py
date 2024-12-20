#Prompt the user for task details
task = input("Enter your task: ").strip()
priority = input("Priority (high/medium/low):").strip().lower()
time_bound = input("Is it time_bound? (yes/no):").strip().lower()
#Process the input using Match Case
match priority:
    case "high":
        reminder = f"'{task}' is a high priority task."
    case "medium":
        reminder = f"'{task}' is a medium priority task."
    case "low":
        reminder = f"'{task}' is a low priority task."
    case _:
        reminder = f"'{task}' has an unknown priority. Please review."
#Modify the reminder if the task is time-bound
if time_bound == "yes":
    reminder += "This requires immediate attention today!"
else:
    reminder+= "Consider completing it when you have free time."
#Output the customized reminder 
print("\nReminder:", reminder)
