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
#Process the input
    if priority == "high":
        reminder = f"'{task}' is a high priority task."
    elif pririoty == "medium":
        reminder = f"'{task}' is a medium priority task."
    elif pririoty == "low":
        reminder = f"'{task}' is a low priority task."
    else:
        reminder = f"'{task}' has an unknown priority. Please review."
#Modify the reminder if the task is time-bound
if time_bound == "yes":
    reminder += "This requires immediate attention today!"
else:
    reminder+= "Consider completing it when you have free time."
#Output the customized reminder 
print("\nReminder:", reminder)
