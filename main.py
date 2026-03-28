# Student Management System
# Developed by: Anuj Yadav
# Language: Python
# Storage: CSV File

import csv
import os

FILE_NAME = "students.csv"

# ---------- CREATE FILE IF NOT EXISTS ----------
if not os.path.exists(FILE_NAME):
    with open(FILE_NAME, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Name", "Age", "Roll Number", "Course"])


# ---------- ADD STUDENT ----------
def add_student(name, age, roll, course):
    with open(FILE_NAME, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([name, age, roll, course])

    print("✅ Student added successfully!")


# ---------- VIEW STUDENTS ----------
def view_students():
    with open(FILE_NAME, "r") as file:
        reader = csv.reader(file)
        next(reader)

        print("\n--- Student List ---")
        for row in reader:
            print(f"Name: {row[0]}, Age: {row[1]}, Roll: {row[2]}, Course: {row[3]}")


# ---------- SEARCH STUDENT ----------
def search_student(name):
    found = False

    with open(FILE_NAME, "r") as file:
        reader = csv.reader(file)
        next(reader)

        for row in reader:
            if row[0].lower() == name.lower():
                print("✅ Student Found:", row)
                found = True

    if not found:
        print("❌ Student not found")


# ---------- UPDATE STUDENT ----------
def update_student(name, age, roll, course):
    rows = []

    with open(FILE_NAME, "r") as file:
        reader = csv.reader(file)
        rows = list(reader)

    updated = False

    for i in range(1, len(rows)):
        if rows[i][0].lower() == name.lower():
            rows[i] = [name, age, roll, course]
            updated = True

    with open(FILE_NAME, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(rows)

    if updated:
        print("✅ Student updated")
    else:
        print("❌ Student not found")


# ---------- DELETE STUDENT ----------
def delete_student(name):
    rows = []

    with open(FILE_NAME, "r") as file:
        reader = csv.reader(file)
        rows = list(reader)

    new_rows = [rows[0]]  # keep header
    deleted = False

    for row in rows[1:]:
        if row[0].lower() != name.lower():
            new_rows.append(row)
        else:
            deleted = True

    with open(FILE_NAME, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(new_rows)

    if deleted:
        print("✅ Student deleted")
    else:
        print("❌ Student not found")


# ---------- MENU ----------
while True:
    print("\n===== Student Management System =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")
    
    choice = input("Enter choice: ")

    if choice == "1":
        name = input("Name: ")
        age = input("Age: ")
        roll = input("Roll Number: ")
        course = input("Course: ")
        add_student(name, age, roll, course)

    elif choice == "2":
        view_students()

    elif choice == "3":
        name = input("Enter name to search: ")
        search_student(name)

    elif choice == "4":
        name = input("Enter name to update: ")
        age = input("New Age: ")
        roll = input("New Roll Number: ")
        course = input("New Course: ")
        update_student(name, age, roll, course)

    elif choice == "5":
        name = input("Enter name to delete: ")
        delete_student(name)

    elif choice == "6":
        print("Exiting program...")
        break

    else:
        print("Invalid choice")
