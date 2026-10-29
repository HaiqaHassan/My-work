
print("=== My AI Study Planner ===")

name = input("Enter your name: ")
goal = input("What is your AI learning goal? ")

while True:
    try:
        days = int(input("How many days per week will you study (1-7)? "))
        if 1 <= days <= 7:
            break
        print("Please enter a number from 1 to 7.")
    except ValueError:
        print("Please enter a whole number.")

while True:
    try:
        hours = float(input("How many hours will you study each day? "))
        if hours > 0:
            break
        print("Please enter a number greater than zero.")
    except ValueError:
        print("Please enter a valid number.")

total_hours = days * hours

plan = f"""
MY AI STUDY PLAN
================
Student Name: {name}
AI Learning Goal: {goal}
Study Days Per Week: {days}
Daily Study Hours: {hours:g}
Total Weekly Study Hours: {total_hours:g}

Keep learning and stay consistent!
"""

print(plan)

with open("study_plan.txt", "w") as file:
    file.write(plan)

print("Your plan has been saved to study_plan.txt")

