employee = {
    "E001": {"name": "Alice", "department": "Engineering", "salary": 7000},
    "E002": {"name": "Zoey", "department": "HR", "salary": 6000},
    "E003": {"name": "Sara", "department": "Operations", "salary": 5000}
}

for id, details in employee.items():
    if details["department"]=="Engineering":
        details["salary"] *= 1.1
print(employee)

user_choice = input("Enter the employee to delete: ")
if user_choice.upper() in employee:
    del employee[user_choice.upper()]
else:
    print("Employee ID not found!")
print(employee)


