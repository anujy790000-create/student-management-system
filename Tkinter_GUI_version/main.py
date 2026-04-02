import tkinter as tk
from tkinter import messagebox, simpledialog
from tkinter import ttk

# Import all functions from student_manager library
from student_manager import add_student, view_students, search_student, update_student, delete_student

# ---------- COLOR THEME ----------
BG_COLOR = "#1e1e2f"
BTN_COLOR = "#4a90e2"
TEXT_COLOR = "white"
ACCENT_COLOR = "#0f3460"

# Set the theme to clam
style = ttk.Style()
style.theme_use('clam')


# ---------- HELPER FUNCTIONS ----------

def clear_window():
    """Clear all widgets from the main window"""
    for widget in root.winfo_children():
        widget.destroy()


def show_menu():
    """Show the main menu"""
    clear_window()
    
    root.configure(bg=BG_COLOR)
    
    # Title
    title_label = tk.Label(root, text="Student Management System", font=("Arial", 16, "bold"), bg=BG_COLOR, fg=TEXT_COLOR)
    title_label.pack(pady=20)
    
    # Subtitle
    subtitle_label = tk.Label(root, text="Select an option below:", font=("Arial", 12), bg=BG_COLOR, fg=TEXT_COLOR)
    subtitle_label.pack(pady=10)
    
    # Menu Buttons
    button_width = 25
    button_height = 2
    button_padx = 10
    button_pady = 10
    
    tk.Button(root, text="➕ Add Student", command=show_add_student, bg=BTN_COLOR, fg=TEXT_COLOR, width=button_width, height=button_height).pack(pady=button_pady)
    
    tk.Button(root, text="👀 View All Students", command=show_view_students, bg=BTN_COLOR, fg=TEXT_COLOR, width=button_width, height=button_height).pack(pady=button_pady)
    
    tk.Button(root, text="🔍 Search Student", command=show_search_student, bg=BTN_COLOR, fg=TEXT_COLOR, width=button_width, height=button_height).pack(pady=button_pady)
    
    tk.Button(root, text="✏️ Update Student", command=show_update_student, bg=BTN_COLOR, fg=TEXT_COLOR, width=button_width, height=button_height).pack(pady=button_pady)
    
    tk.Button(root, text="🗑️ Delete Student", command=show_delete_student, bg=BTN_COLOR, fg=TEXT_COLOR, width=button_width, height=button_height).pack(pady=button_pady)
    
    tk.Button(root, text="ℹ️ About", command=show_about, bg=BTN_COLOR, fg=TEXT_COLOR, width=button_width, height=button_height).pack(pady=button_pady)
    
    # Exit Button
    tk.Button(root, text="Exit", command=root.quit, bg=ACCENT_COLOR, fg=TEXT_COLOR, width=button_width).pack(pady=20)


def show_about():
    """Show the About section"""
    clear_window()
    
    root.configure(bg=BG_COLOR)
    
    tk.Label(root, text="About", font=("Arial", 14, "bold"), bg=BG_COLOR, fg=TEXT_COLOR).pack(pady=10)
    
    # Create frame for about content
    frame = tk.Frame(root, bg=BG_COLOR)
    frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
    
    about_text = tk.Text(frame, height=15, width=70, wrap=tk.WORD, bg=ACCENT_COLOR, fg=TEXT_COLOR)
    about_text.pack(fill=tk.BOTH, expand=True)
    
    about_content = """
STUDENT MANAGEMENT SYSTEM
Version 1.0

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

DEVELOPED BY:
Anuj Yadav

LANGUAGE:
Python 3

DATABASE:
CSV File (students.csv)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

FEATURES:

✓ Add Student - Add new student records
✓ View All Students - Display all students
✓ Search Student - Find student by name
✓ Update Student - Modify student details
✓ Delete Student - Remove student records

DESCRIPTION:

This is a simple yet powerful Student Management 
System designed to help manage student records 
efficiently. The application provides a user-friendly 
interface with all the essential features for 
maintaining student information.

All student data is stored in a CSV file for easy 
portability and compatibility.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
"""
    
    about_text.insert("1.0", about_content)
    about_text.config(state=tk.DISABLED)
    
    tk.Button(root, text="Back to Menu", command=show_menu, bg=BTN_COLOR, fg=TEXT_COLOR, width=20).pack(pady=10)


def show_add_student():
    """Show the add student form"""
    clear_window()
    
    root.configure(bg=BG_COLOR)
    
    tk.Label(root, text="Add Student", font=("Arial", 14, "bold"), bg=BG_COLOR, fg=TEXT_COLOR).pack(pady=10)
    
    tk.Label(root, text="Name", bg=BG_COLOR, fg=TEXT_COLOR).pack(pady=5)
    name_entry = tk.Entry(root, width=30, bg=ACCENT_COLOR, fg=TEXT_COLOR)
    name_entry.pack(pady=5)
    
    tk.Label(root, text="Roll Number", bg=BG_COLOR, fg=TEXT_COLOR).pack(pady=5)
    roll_entry = tk.Entry(root, width=30, bg=ACCENT_COLOR, fg=TEXT_COLOR)
    roll_entry.pack(pady=5)
    
    tk.Label(root, text="Course", bg=BG_COLOR, fg=TEXT_COLOR).pack(pady=5)
    course_entry = tk.Entry(root, width=30, bg=ACCENT_COLOR, fg=TEXT_COLOR)
    course_entry.pack(pady=5)
    
    tk.Label(root, text="Age (Optional)", bg=BG_COLOR, fg=TEXT_COLOR).pack(pady=5)
    age_entry = tk.Entry(root, width=30, bg=ACCENT_COLOR, fg=TEXT_COLOR)
    age_entry.pack(pady=5)
    
    def submit():
        name = name_entry.get()
        roll = roll_entry.get()
        course = course_entry.get()
        age = age_entry.get() if age_entry.get() else "N/A"
        
        if name and roll and course:
            if add_student(name, roll, course, age):
                messagebox.showinfo("Success", "✅ Student added successfully!")
                show_menu()
            else:
                messagebox.showerror("Error", "❌ Failed to add student")
        else:
            messagebox.showwarning("Error", "Please fill in Name, Roll Number, and Course")
    
    button_frame = tk.Frame(root, bg=BG_COLOR)
    button_frame.pack(pady=10)
    
    tk.Button(button_frame, text="Add Student", command=submit, bg=BTN_COLOR, fg=TEXT_COLOR, width=15).pack(side=tk.LEFT, padx=5)
    tk.Button(button_frame, text="Back to Menu", command=show_menu, bg=ACCENT_COLOR, fg=TEXT_COLOR, width=15).pack(side=tk.LEFT, padx=5)


def show_view_students():
    """Show all students"""
    clear_window()
    
    root.configure(bg=BG_COLOR)
    
    tk.Label(root, text="All Students", font=("Arial", 14, "bold"), bg=BG_COLOR, fg=TEXT_COLOR).pack(pady=10)
    
    # Create frame for text widget and scrollbar
    frame = tk.Frame(root, bg=BG_COLOR)
    frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
    
    scrollbar = tk.Scrollbar(frame)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    
    output = tk.Text(frame, height=15, width=70, yscrollcommand=scrollbar.set, bg=ACCENT_COLOR, fg=TEXT_COLOR)
    output.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
    scrollbar.config(command=output.yview)
    
    students = view_students()
    
    if students:
        for idx, student in enumerate(students, 1):
            output.insert(tk.END, f"{idx}. {student}\n")
    else:
        output.insert(tk.END, "No students found in the database.")
    
    output.config(state=tk.DISABLED)
    
    tk.Button(root, text="Back to Menu", command=show_menu, bg=BTN_COLOR, fg=TEXT_COLOR, width=20).pack(pady=10)


def show_search_student():
    """Show the search student form"""
    clear_window()
    
    root.configure(bg=BG_COLOR)
    
    tk.Label(root, text="Search Student", font=("Arial", 14, "bold"), bg=BG_COLOR, fg=TEXT_COLOR).pack(pady=10)
    
    tk.Label(root, text="Enter Student Name", bg=BG_COLOR, fg=TEXT_COLOR).pack(pady=5)
    search_entry = tk.Entry(root, width=30, bg=ACCENT_COLOR, fg=TEXT_COLOR)
    search_entry.pack(pady=5)
    
    results_text = tk.Text(root, height=12, width=70, bg=ACCENT_COLOR, fg=TEXT_COLOR)
    
    def search():
        name = search_entry.get()
        
        if not name:
            messagebox.showwarning("Error", "Please enter a student name")
            return
        
        results = search_student(name)
        
        results_text.pack(pady=5)
        results_text.config(state=tk.NORMAL)
        results_text.delete("1.0", tk.END)
        
        if results:
            results_text.insert(tk.END, f"Found {len(results)} student(s):\n\n")
            for result in results:
                results_text.insert(tk.END, f"Name: {result[0]}\nAge: {result[1]}\nRoll: {result[2]}\nCourse: {result[3]}\n" + "-"*40 + "\n")
        else:
            results_text.insert(tk.END, f"❌ No student found with name: {name}")
        
        results_text.config(state=tk.DISABLED)
    
    tk.Button(root, text="Search", command=search, bg=BTN_COLOR, fg=TEXT_COLOR, width=20).pack(pady=10)
    
    tk.Button(root, text="Back to Menu", command=show_menu, bg=ACCENT_COLOR, fg=TEXT_COLOR, width=20).pack(pady=10)


def show_update_student():
    """Show the update student form"""
    clear_window()
    
    root.configure(bg=BG_COLOR)
    
    tk.Label(root, text="Update Student", font=("Arial", 14, "bold"), bg=BG_COLOR, fg=TEXT_COLOR).pack(pady=10)
    
    tk.Label(root, text="Student Name (to find)", bg=BG_COLOR, fg=TEXT_COLOR).pack(pady=5)
    name_entry = tk.Entry(root, width=30, bg=ACCENT_COLOR, fg=TEXT_COLOR)
    name_entry.pack(pady=5)
    
    tk.Label(root, text="New Age", bg=BG_COLOR, fg=TEXT_COLOR).pack(pady=5)
    age_entry = tk.Entry(root, width=30, bg=ACCENT_COLOR, fg=TEXT_COLOR)
    age_entry.pack(pady=5)
    
    tk.Label(root, text="New Roll Number", bg=BG_COLOR, fg=TEXT_COLOR).pack(pady=5)
    roll_entry = tk.Entry(root, width=30, bg=ACCENT_COLOR, fg=TEXT_COLOR)
    roll_entry.pack(pady=5)
    
    tk.Label(root, text="New Course", bg=BG_COLOR, fg=TEXT_COLOR).pack(pady=5)
    course_entry = tk.Entry(root, width=30, bg=ACCENT_COLOR, fg=TEXT_COLOR)
    course_entry.pack(pady=5)
    
    def submit():
        name = name_entry.get()
        age = age_entry.get()
        roll = roll_entry.get()
        course = course_entry.get()
        
        if name and age and roll and course:
            if update_student(name, age, roll, course):
                messagebox.showinfo("Success", "✅ Student updated successfully!")
                show_menu()
            else:
                messagebox.showerror("Error", "❌ Student not found")
        else:
            messagebox.showwarning("Error", "Please fill in all fields")
    
    button_frame = tk.Frame(root, bg=BG_COLOR)
    button_frame.pack(pady=10)
    
    tk.Button(button_frame, text="Update Student", command=submit, bg=BTN_COLOR, fg=TEXT_COLOR, width=15).pack(side=tk.LEFT, padx=5)
    tk.Button(button_frame, text="Back to Menu", command=show_menu, bg=ACCENT_COLOR, fg=TEXT_COLOR, width=15).pack(side=tk.LEFT, padx=5)


def show_delete_student():
    """Show the delete student form"""
    clear_window()
    
    root.configure(bg=BG_COLOR)
    
    tk.Label(root, text="Delete Student", font=("Arial", 14, "bold"), bg=BG_COLOR, fg=TEXT_COLOR).pack(pady=20)
    
    tk.Label(root, text="Enter Student Name to Delete", bg=BG_COLOR, fg=TEXT_COLOR).pack(pady=10)
    name_entry = tk.Entry(root, width=30, bg=ACCENT_COLOR, fg=TEXT_COLOR)
    name_entry.pack(pady=5)
    
    def submit():
        name = name_entry.get()
        
        if not name:
            messagebox.showwarning("Error", "Please enter a student name")
            return
        
        # Confirmation dialog
        confirm = messagebox.askyesno("Confirm", f"Are you sure you want to delete {name}?")
        
        if confirm:
            if delete_student(name):
                messagebox.showinfo("Success", "✅ Student deleted successfully!")
                show_menu()
            else:
                messagebox.showerror("Error", "❌ Student not found")
    
    button_frame = tk.Frame(root, bg=BG_COLOR)
    button_frame.pack(pady=20)
    
    tk.Button(button_frame, text="Delete Student", command=submit, bg=BTN_COLOR, fg=TEXT_COLOR, width=15).pack(side=tk.LEFT, padx=5)
    tk.Button(button_frame, text="Back to Menu", command=show_menu, bg=ACCENT_COLOR, fg=TEXT_COLOR, width=15).pack(side=tk.LEFT, padx=5)


# ---------- MAIN WINDOW ----------

root = tk.Tk()
root.title("Student Management System")
root.geometry("600x600")
root.configure(bg=BG_COLOR)

# Show the main menu on startup
show_menu()

# ---------- RUN APP ----------
root.mainloop()
