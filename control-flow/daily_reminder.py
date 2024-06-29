# This program that uses conditionals, match case and loops to remind the user

task = input("Input a task: ")
priority = input("Enter its priority level(high, medium, low): ")
time_bound = input("Is it time bound? (yes/no): ")

match priority:
    case "high":
        if time_bound == "yes":
            print(f"Reminder! {task} is a {priority} priority task that requires immediate attention today!")
        else:
            print(f"Reminder: {task} is a {priority} priority task but find time  attention today!")
    case "medium":
        if time_bound == "yes":
            print(f"Reminder! {task} is a {priority} priority task that requires attention a few days")
        else:
            print(f"Reminder! {task} is a {priority} priority task that requires some today!")
    case "low":
        if time_bound == "yes":
            print(f"Note: {task} is a low priority task. Consider completing it when you have free time.")
        else:
            print(f"Note: {task} is a low priority task. Consider completing it when you have free time.")


