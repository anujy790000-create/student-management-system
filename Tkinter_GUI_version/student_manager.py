# Student Management System Library
# Developed by: Anuj Yadav
# Language: Python
# Storage: CSV File

import csv
import os

FILE_NAME = "students.csv"


# ---------- INITIALIZE FILE ----------
def _initialize_file():
    """Initialize CSV file if it doesn't exist."""
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Name", "Age", "Roll Number", "Course"])


# Initialize on module load
_initialize_file()


# ---------- ADD STUDENT ----------
def add_student(name, roll, course, age="N/A"):
    """Add a student to the CSV file.
    
    Args:
        name (str): Student name
        roll (str): Roll number
        course (str): Course name
        age (str): Age of student (optional, defaults to 'N/A')
    
    Returns:
        bool: True if student was added successfully
    """
    try:
        with open(FILE_NAME, "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([name, age, roll, course])
        return True
    except Exception as e:
        print(f"Error adding student: {e}")
        return False


# ---------- VIEW STUDENTS ----------
def view_students():
    """Retrieve all students from the CSV file.
    
    Returns:
        list: List of student records as strings
    """
    students = []
    try:
        with open(FILE_NAME, "r") as file:
            reader = csv.reader(file)
            next(reader)  # Skip header
            for row in reader:
                students.append(f"Name: {row[0]}, Age: {row[1]}, Roll: {row[2]}, Course: {row[3]}")
    except FileNotFoundError:
        pass
    return students


# ---------- SEARCH STUDENT ----------
def search_student(name):
    """Search for a student by name.
    
    Args:
        name (str): Student name to search for
    
    Returns:
        list: List of matching student records, or empty list if not found
    """
    results = []
    try:
        with open(FILE_NAME, "r") as file:
            reader = csv.reader(file)
            next(reader)  # Skip header
            for row in reader:
                if row[0].lower() == name.lower():
                    results.append(row)
    except FileNotFoundError:
        pass
    return results


# ---------- UPDATE STUDENT ----------
def update_student(name, age, roll, course):
    """Update an existing student's information.
    
    Args:
        name (str): Student name to update
        age (str): New age
        roll (str): New roll number
        course (str): New course
    
    Returns:
        bool: True if student was updated, False if not found
    """
    rows = []
    try:
        with open(FILE_NAME, "r") as file:
            reader = csv.reader(file)
            rows = list(reader)

        updated = False
        for i in range(1, len(rows)):
            if rows[i][0].lower() == name.lower():
                rows[i] = [name, age, roll, course]
                updated = True
                break

        with open(FILE_NAME, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerows(rows)

        return updated
    except Exception as e:
        print(f"Error updating student: {e}")
        return False


# ---------- DELETE STUDENT ----------
def delete_student(name):
    """Delete a student from the CSV file.
    
    Args:
        name (str): Student name to delete
    
    Returns:
        bool: True if student was deleted, False if not found
    """
    rows = []
    try:
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

        return deleted
    except Exception as e:
        print(f"Error deleting student: {e}")
        return False
