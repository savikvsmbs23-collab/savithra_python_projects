students = ["Alice", "Bob", "Zoey"]

def greeting(wish, students):
    for student in students:
        print(f"{wish} {student}!")

print("--- Morning Class ---")
greeting("Good morning", students)

print("--- Evening Class ---")
greeting("Good evening", students)

print("--- Night Class ---")
greeting("Good night", students)
