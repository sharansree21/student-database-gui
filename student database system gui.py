import tkinter as tk
from tkinter import messagebox

class StudentDatabaseApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Database System")

        # Create labels
        self.label_name = tk.Label(root, text="Name:")
        self.label_roll = tk.Label(root, text="Roll Number:")
        self.label_grade = tk.Label(root, text="Grade:")

        # Create entry widgets
        self.entry_name = tk.Entry(root)
        self.entry_roll = tk.Entry(root)
        self.entry_grade = tk.Entry(root)

        # Create buttons
        self.button_add = tk.Button(root, text="Add Student", command=self.add_student)
        self.button_display = tk.Button(root, text="Display Students", command=self.display_students)

        # Grid layout
        self.label_name.grid(row=0, column=0)
        self.label_roll.grid(row=1, column=0)
        self.label_grade.grid(row=2, column=0)

        self.entry_name.grid(row=0, column=1)
        self.entry_roll.grid(row=1, column=1)
        self.entry_grade.grid(row=2, column=1)

        self.button_add.grid(row=3, column=0, columnspan=2, pady=10)
        self.button_display.grid(row=4, column=0, columnspan=2, pady=10)

        # Student database
        self.students = []

    def add_student(self):
        name = self.entry_name.get()
        roll = self.entry_roll.get()
        grade = self.entry_grade.get()

        if name and roll and grade:
            student_info = f"Name: {name}, Roll Number: {roll}, Grade: {grade}"
            self.students.append(student_info)
            messagebox.showinfo("Success", "Student added successfully!")
            self.clear_entries()
        else:
            messagebox.showerror("Error", "Please fill in all the fields.")

    def display_students(self):
        if self.students:
            student_list = "\n".join(self.students)
            messagebox.showinfo("Students", student_list)
        else:
            messagebox.showinfo("No Students", "No students in the database.")

    def clear_entries(self):
        self.entry_name.delete(0, tk.END)
        self.entry_roll.delete(0, tk.END)
        self.entry_grade.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = StudentDatabaseApp(root)
    root.mainloop()
