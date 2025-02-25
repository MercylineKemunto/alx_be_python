#Prompt the user for task details
task = input("Enter your task: ").strip()
#Validate priority input
valid_priorities = ["high", "medium", "low"]
priority = input("Priority (high/medium/low):").strip().lower()
while priority not in valid_priorities:
    print("Invalid priority! Please choose from high, medium, or low.")
    priority = input("Priority (high/medium/low):").strip().lower()
#Validate time-bound input
valid_time_bound = ["yes", "no"]
time_bound = input("Is it time-bound? (yes/no):").strip().lower()
while time_bound not in valid_time_bound:
    print("Invalid response! Please answer yes or no.")
    time_bound = input("Is it time bound? (yes/no):").strip().lower()
#Match-case for priority
match priority:
    case "high":
        reminder = f"'{task}' is a high priority task."
    case "medium":
        reminder = f"'{task}' is a medium priority task."
    case  "low":
        reminder = f"'{task}' is a low priority task."
    case _:
        reminder = f"'{task}' has an unknown priority. Please review."
#Add time-bound condition
if time_bound == "yes":
    reminder += "This requires immediate attention today!"
else:
    reminder+= "Consider completing it when you have free time."
#Display the final reminder
print(f"Reminder: {reminder}")
