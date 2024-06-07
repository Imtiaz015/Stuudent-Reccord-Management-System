import tkinter as tk
from tkinter import ttk

class Student:
    def __init__(self, name, fname, roll_number, marks):
        self.name = name
        self.fname = fname
        self.roll_number = roll_number
        self.marks = marks

class StudentRecordApp:
    def __init__(self, master):
        self.master = master
        self.master.title('"Student Record Management System"')
        self.master.configure(bg='black')

        self.students = []

        self.style = ttk.Style()
        self.style.configure('TButton', padding=10, font=('Helvetica', 12, 'bold'), foreground='green', background='black',
                             bordercolor='red', borderwidth=3)
        self.label_style = ttk.Style()
        self.label_style.configure('TLabel', foreground='white', background='black', font=('Helvetica', 16, 'bold'))
        self.frame_style = ttk.Style()
        self.frame_style.configure('TFrame', background='black')

        self.label = ttk.Label(master, text="Welcome to Student Record Management System")
        self.label.pack(pady=20)

        self.frame = ttk.Frame(master, style='TFrame')
        self.frame.pack(pady=10)

        self.button_add = ttk.Button(self.frame, text="Add Student", command=self.add_student)
        self.button_add.pack(side=tk.LEFT, padx=5)

        self.button_view = ttk.Button(self.frame, text="View Students", command=self.view_students)
        self.button_view.pack(side=tk.LEFT, padx=5)

        self.button_update = ttk.Button(self.frame, text="Update Student", command=self.update_student_window)
        self.button_update.pack(side=tk.LEFT, padx=5)

        self.button_delete = ttk.Button(self.frame, text="Delete Student", command=self.delete_student_window)
        self.button_delete.pack(side=tk.LEFT, padx=5)

        self.button_search = ttk.Button(self.frame, text="Search Student", command=self.search_student_window)
        self.button_search.pack(side=tk.LEFT, padx=5)

        self.button_exit = ttk.Button(master, text="Exit", command=master.quit)
        self.button_exit.pack(pady=10)

        # Add the label at the bottom
        self.creator_label = ttk.Label(master, text="THIS APPLICATION IS CREATED BY : IMTIAZ ALI MAITLO", font=("Helvetica", 10, 'bold'), background='black', foreground='white')
        self.creator_label.pack(side=tk.BOTTOM, pady=10)

    def add_student(self):
        add_window = tk.Toplevel(self.master)
        add_window.title("Add Student")

        # Create labels and entry widgets for user input in the new window
        name_label = ttk.Label(add_window, text="Enter Student Name:", font=('Helvetica', 12, 'bold'))
        name_label.pack(padx=10, pady=5)
        self.name_entry = ttk.Entry(add_window)
        self.name_entry.pack(padx=10, pady=5)

        fname_label = ttk.Label(add_window, text="Enter Father's Name:", font=('Helvetica', 12, 'bold'))
        fname_label.pack(padx=10, pady=5)
        self.fname_entry = ttk.Entry(add_window)
        self.fname_entry.pack(padx=10, pady=5)

        roll_label = ttk.Label(add_window, text="Enter Roll Number:", font=('Helvetica', 12, 'bold'))
        roll_label.pack(padx=10, pady=5)
        self.roll_entry = ttk.Entry(add_window)
        self.roll_entry.pack(padx=10, pady=5)

        marks_label = ttk.Label(add_window, text="Enter Marks:", font=('Helvetica', 12, 'bold'))
        marks_label.pack(padx=10, pady=5)
        self.marks_entry = ttk.Entry(add_window)
        self.marks_entry.pack(padx=10, pady=5)

        # Create a button to execute the add function
        add_button = ttk.Button(add_window, text="Add", command=self.add)
        add_button.pack(pady=10)

    def add(self):
        # Retrieve input values
        name = self.name_entry.get()
        fname = self.fname_entry.get()
        roll_number = self.roll_entry.get()
        marks = float(self.marks_entry.get())

        # Create Student object and add it to the list
        student = Student(name, fname, roll_number, marks)
        self.students.append(student)
        
        # Optionally, you can clear the entry fields after adding
        self.name_entry.delete(0, tk.END)
        self.fname_entry.delete(0, tk.END)
        self.roll_entry.delete(0, tk.END)
        self.marks_entry.delete(0, tk.END)

        print("Student added successfully!")

    def view_students(self):
        view_window = tk.Toplevel(self.master)
        view_window.title("View Students")

        # Create a Treeview widget to display the student records in a table
        tree = ttk.Treeview(view_window, columns=("S.No", "Name", "Father's Name", "Roll Number", "Marks"), show="headings")
        tree.heading("S.No", text="S.No", anchor=tk.CENTER)
        tree.heading("Name", text="Name", anchor=tk.CENTER)
        tree.heading("Father's Name", text="Father's Name", anchor=tk.CENTER)
        tree.heading("Roll Number", text="Roll Number", anchor=tk.CENTER)
        tree.heading("Marks", text="Marks", anchor=tk.CENTER)
        
        # Insert student records into the Treeview
        for idx, student in enumerate(self.students, start=1):
            tree.insert("", tk.END, values=(idx, student.name, student.fname, student.roll_number, student.marks))
        
        # Set column alignment
        for col in ("S.No", "Name", "Father's Name", "Roll Number", "Marks"):
            tree.column(col, anchor=tk.CENTER)
            
        tree.pack(expand=True, fill="both")

    def update_student_window(self):
        update_window = tk.Toplevel(self.master)
        update_window.title("Update Student")
        roll_label = ttk.Label(update_window, text="Enter  Roll  Number To update   :", font=('Helvetica', 12, 'bold'))
        roll_label.grid(row=0, column=0, padx=10, pady=5)
        self.roll_entry_update = ttk.Entry(update_window)
        self.roll_entry_update.grid(row=0, column=1, padx=10, pady=5)
        name_label = ttk.Label(update_window, text="Enter Student Name To Update :", font=('Helvetica', 12, 'bold'))
        name_label.grid(row=2, column=0, padx=10, pady=5)
        self.name_entry = ttk.Entry(update_window)
        self.name_entry.grid(row=2, column=1, padx=10, pady=5)
        fname_label = ttk.Label(update_window, text="Enter Father Name To  Update   :", font=('Helvetica', 12, 'bold'))
        fname_label.grid(row=1, column=0, padx=10, pady=5)
        self.fname_entry = ttk.Entry(update_window)
        self.fname_entry.grid(row=1, column=1, padx=10, pady=5)
        marks_label = ttk.Label(update_window, text="Enter   The  Marks  To  Update   :", font=('Helvetica', 12, 'bold'))
        marks_label.grid(row=3, column=0, padx=10, pady=5)
        self.marks_entry = ttk.Entry(update_window)
        self.marks_entry.grid(row=3, column=1, padx=10, pady=5)
        update_button = ttk.Button(update_window, text="Update", command=self.update_student)
        update_button.grid(row=4, columnspan=2, padx=10, pady=10)

    
    def update_student(self):
        roll_number = self.roll_entry_update.get()
        for student in self.students:
           if student.roll_number == roll_number:
                # Swap the first name and father's name entries
                updated_fname = self.fname_entry.get()
                updated_name = self.name_entry.get()
                self.fname_entry.delete(0, tk.END)
                self.fname_entry.insert(0, updated_name)
                self.name_entry.delete(0, tk.END)
                self.name_entry.insert(0, updated_fname)
                
                # Update other fields
                student.name = updated_fname
                student.fname = updated_name
                student.marks = float(self.marks_entry.get())
                print("Student record updated successfully!")
                return
    print("Student not found.")


    def delete_student_window(self):
        delete_window = tk.Toplevel(self.master)
        delete_window.title("Delete Student")
        
        roll_label = ttk.Label(delete_window, text="Enter roll number of the student to delete:", font=('Helvetica', 12, 'bold'))
        roll_label.grid(row=0, column=0, padx=10, pady=5)
        self.delete_entry = ttk.Entry(delete_window)
        self.delete_entry.grid(row=0, column=1, padx=10, pady=5)
        delete_button = ttk.Button(delete_window, text="Delete", command=self.delete_student)
        delete_button.grid(row=1, columnspan=2, padx=10, pady=10)

    def delete_student(self):
        roll_number = self.delete_entry.get()
        found = False
        
        for student in self.students:
            if student.roll_number == roll_number:
                self.students.remove(student)
                print(f"Student with roll number {roll_number} deleted successfully!")
                found = True
                break
        
        if not found:
            print("Student not found.")

    def search_student_window(self):
        search_window = tk.Toplevel(self.master)
        search_window.title("Search Student")
        
        roll_label = ttk.Label(search_window, text="Enter roll number of the student to search:", font=('Helvetica', 12, 'bold'))
        roll_label.grid(row=0, column=0, padx=10, pady=5)
        self.search_entry = ttk.Entry(search_window)
        self.search_entry.grid(row=0, column=1, padx=10, pady=5)
        search_button = ttk.Button(search_window, text="Search", command=self.search_student)
        search_button.grid(row=1, columnspan=2, padx=10, pady=10)
    
    def search_student(self):
        roll_number = self.search_entry.get()
        found = False
        
        # Create a new Toplevel window to display search result
        search_result_window = tk.Toplevel(self.master)
        search_result_window.title("Search Result")
        
        # Create a Treeview widget to display the student record
        tree = ttk.Treeview(search_result_window, columns=("Name", "Father's Name", "Roll Number", "Marks"), show="headings")
        tree.heading("Name", text="Name", anchor=tk.CENTER)
        tree.heading("Father's Name", text="Father's Name", anchor=tk.CENTER)
        tree.heading("Roll Number", text="Roll Number", anchor=tk.CENTER)
        tree.heading("Marks", text="Marks", anchor=tk.CENTER)
        
        # Find and display the student's data
        for student in self.students:
            if student.roll_number == roll_number:
                tree.insert("", tk.END, values=(student.name, student.fname, student.roll_number, student.marks))
                found = True
                break
        
        # If student not found, display a message
        if not found:
            tree.insert("", tk.END, values=("Student not found", "", "", ""))
        
        # Set column alignment
        for col in ("Name", "Father's Name", "Roll Number", "Marks"):
            tree.column(col, anchor=tk.CENTER)
        
        tree.pack(expand=True, fill="both")


root = tk.Tk()
root.attributes('-alpha', 0.9)
app = StudentRecordApp(root)
root.mainloop()
