students = [
    {"name": "Alice", "grade": 85},
    {"name": "Bob", "grade": 42},
    {"name": "Zoey", "grade": 91},
    {"name": "Sam", "grade": 55},
]

def print_students(result, students):
    for student in students:
        if result == "pass":
            if student["grade"] >= 50:
                print(student["name"])
        elif result == "fail":
            if student["grade"] < 50:
                print(student["name"])

def calculate_average(students):
    total = 0
    for student in students:
        total += student["grade"]
    average = total / len(students)
    return average

# Print passed students (grade >= 50)

print("--- Passed ---")
print_students("pass", students)

# Print failed students (grade < 50)

print("--- Failed ---")
print_students("fail", students)

# # Print average grade

print(f"Class average: {calculate_average(students)}")


