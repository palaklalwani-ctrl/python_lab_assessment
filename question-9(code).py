# Student Grading System

students = []

number_of_students = int(input("Enter number of students: "))

for i in range(number_of_students):
    print(f"\nStudent {i + 1}")
    name = input("Enter student name: ")
    marks = float(input("Enter marks out of 100: "))

    if marks < 0 or marks > 100:
        print("Invalid marks. Please enter marks between 0 and 100.")
        continue

    if marks >= 90:
        grade = "A+"
    elif marks >= 80:
        grade = "A"
    elif marks >= 70:
        grade = "B"
    elif marks >= 60:
        grade = "C"
    elif marks >= 50:
        grade = "D"
    else:
        grade = "F"

    students.append({"name": name, "marks": marks, "grade": grade})

print("\n--- Student Results ---")
for student in students:
    print(student["name"], "- Marks:", student["marks"], "- Grade:", student["grade"])
