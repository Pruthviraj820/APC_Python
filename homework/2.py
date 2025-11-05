students = []
grades = []

def add_student(name, grade):
    students.append(name)
    grades.append(grade)
    print(f"Added {name} with grade {grade}.")

def update_grade(name, new_grade):
    if name in students:
        index = students.index(name)
        grades[index] = new_grade
        print(f"Updated {name}'s grade to {new_grade}.")
    else:
        print(f"Student {name} not found.")

def remove_student(name):
    if name in students:
        index = students.index(name)
        students.pop(index)
        grades.pop(index)
        print(f"Removed {name}.")
    else:
        print(f"Student {name} not found.")

def calculate_average():
    if grades:
        avg = sum(grades) / len(grades)
        print(f"Average grade: {avg:.2f}")
    else:
        print("No grades available.")

def display_highest_lowest():
    if grades:
        highest = max(grades)
        lowest = min(grades)
        print(f"Highest grade: {highest}")
        print(f"Lowest grade: {lowest}")
    else:
        print("No grades available.")

while True:
    print("\n--- Student Grade Management ---")
    print("1. Add Student")
    print("2. Update Grade")
    print("3. Remove Student")
    print("4. Calculate Average Grade")
    print("5. Display Highest and Lowest Grades")
    print("6. Exit")
    
    choice = input("Enter choice (1-6): ")
    
    if choice == '1':
        name = input("Enter student name: ")
        grade = float(input("Enter grade: "))
        add_student(name, grade)
    elif choice == '2':
        name = input("Enter student name to update: ")
        new_grade = float(input("Enter new grade: "))
        update_grade(name, new_grade)
    elif choice == '3':
        name = input("Enter student name to remove: ")
        remove_student(name)
    elif choice == '4':
        calculate_average()
    elif choice == '5':
        display_highest_lowest()
    elif choice == '6':
        print("Exiting program...")
        break
    else:
        print("Invalid choice! Please try again.")
