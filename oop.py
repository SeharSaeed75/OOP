# University class
import random

class University:
    def __init__(self, name):
        self.name = name
        self.departments = []
        self.teachers = []
        self.students = []

    def add_department(self, department, silent=False):
        self.departments.append(department)
        if not silent:
            print(f"Department '{department}' add.")
    
    def get_departments(self):
        print("Departments:")
        for dept in self.departments:
            print(dept)

    def remove_department(self, department):
        if department in self.departments:
            self.departments.remove(department)
            print(f"Department '{department}' remove.")
        else:
            print(f"Department '{department}' not found.")


    def add_teacher(self, teacher, silent=False):
        self.teachers.append(teacher)
        if not silent:
            print(f"Teacher {teacher.name} add.")

    def get_teachers(self):
        print("Teachers:")
        for teacher in self.teachers:
            print(teacher.name)

    def add_student(self, student, silent=False):
        self.students.append(student)
        if not silent:
            print(f"Student '{student.name}' add.")
    
    def get_students(self):
        print("Students:")
        for student in self.students:
            print(student.name)

# Human class inherite from Univeristy class
class Human(University):
    def __init__(self, name, id, age, contact):
        self.name = name
        self.id = id
        self.age = age
        self.contact = contact
        

# Teacher class inherite from Human class
class Teacher(Human):
    def __init__(self, name, id, age, contact, departments):
        super().__init__(name, id, age, contact)
        self.departments = departments

    def schedule(self):
        print("Class Schedule:")
        print("Saturday: 2 PM - 6 PM")
        print("Sunday: 2 PM - 6 PM")

# Student class inherite from Human class
class Student(Human):
    def __init__(self, name, id, age, contact, department, semester, courses):
        super().__init__(name, id, age, contact)
        self.department = department
        self.semester = semester
        self.courses = courses

    def show_student_info(self):
        print(f"Name: {self.name}")
        print(f"ID: {self.id}")
        print(f"Age: {self.age}")
        print(f"Department: {self.department}")
        print(f"Semester: {self.semester}")
        print(f"Courses: {', '.join(self.courses)}")

# Admin class inherite from Human class
class Admin(Human):
    def __init__(self, name, id, age, contact):
        super().__init__(name, id, age, contact)

    def add_teacher(self, university):
        name = input("Enter teacher name: ")
        age = int(input("Enter teacher age: "))
        contact = input("Enter teacher contact: ")
        department = input("Enter department for the teacher: ")

        if department in university.departments:
            new_teacher = Teacher(name, age, "Teacher", contact, [department])
            university.add_teacher(new_teacher)
            print(f"Teacher {name} added to department {department}.")
        else:
            print(f"Department '{department}' not found. Please add the department first.")



def random_student():
    names = ["Sehar", "Menahil", "Eman" ]
    departments = ["Computer Science"]
    courses = ["WEb programming", "Genrative AI" ]
    
    name = random.choice(names)
    age = random.randint(20, 25)
    contact = f"555{random.randint(1000000, 9999999)}"
    department = random.choice(departments)
    semester = f"Semester {random.randint(1, 8)}"
    selected_courses = random.sample(courses, 2)

    return Student(name, "Student", age, contact, department, semester, selected_courses)

def uni():
    university = University("PIAIC")
    university.add_department("Computer Science", silent=True)
    university.add_department("Artificial Intelligence", silent=True)

    teacher1 = Teacher("Naveed Sarwar", "Teacher", 28, "9876543210", ["Genrative AI"])
    teacher2 = Teacher("Abu Hurairah", "Teacher", 24, "6385381247",["Web programming"])

    university.add_teacher(teacher1, silent=True)
    university.add_teacher(teacher2, silent=True)

    # Add 4 random students without printing messages
    for _ in range(4):
        university.add_student(random_student(), silent=True)

    while True:
        print("\n_-_-_-_-_-_-_-_-_-_- PIAIC  _-_-_-_-_-_-_-_-_-_-\n")
        print("Select your ID:")
        print("1. Admin")
        print("2. Teacher")
        print("3. Student")
        print("4. Exit")

        choice = input("Enter your choice (1/2/3/4): ")

        if choice == '1':
            print("You are an Admin!")
            admin = Admin("Zia Khan", "Admin", 51, "5555555555")
            while True:
                print("\n_______Admin Options_______")
                print("1. View Departments")
                print("2. Add Department")
                print("3. Remove Department")
                print("4. Add Teacher")
                print("5. Add Student")
                print("6. Exit")

                admin_choice = input("Enter your choice: ")

                if admin_choice == '1':
                    university.get_departments()
                elif admin_choice == '2':
                    dept_name = input("Enter the name of the department to add: ")
                    university.add_department(dept_name)
                elif admin_choice == '3':
                    dept_name = input("Enter the name of the department to remove: ")
                    university.remove_department(dept_name)
                elif admin_choice == '4':
                    admin.add_teacher(university)
                elif admin_choice == '5':
                    student_name = input("Enter student name: ")
                    for student in university.students:
                        if student.name == student_name:
                            print("Student already exists!")
                            break
                    else:
                        new_student = random_student()
                        university.add_student(new_student)
                elif admin_choice == '6':
                    break
                else:
                    print("Invalid choice!")

        elif choice == '2':
            teacher_name = input("Enter teacher name (Naveed Sarwar, Abu Hurairah ): ")
            for teacher in university.teachers:
                if teacher.name == teacher_name:
                    print(f"Welcome {teacher.name}!")
                    while True:
                        print("\n_______Teacher Options_______")
                        print("1. View Departments")
                        print("2. View Class Schedule")
                        print("3. Exit")

                        teacher_choice = input("Enter your choice (1/2/3): ")

                        if teacher_choice == '1':
                            print(f"Departments: {', '.join(teacher.departments)}")
                        elif teacher_choice == '2':
                            teacher.schedule()
                        elif teacher_choice == '3':
                            break
                        else:
                            print("Invalid choice!")
                    break
            else:
                print("Teacher not found.")

        elif choice == '3':
            print("You are a Student!")
            student_name = input("Enter student name: ")
            for student in university.students:
                if student.name == student_name:
                    print(f"Welcome {student.name}!")
                    while True:
                        print("\n_______Student Options_______")
                        print("1. View Student Details")
                        print("2. Exit")

                        student_choice = input("Enter your choice (1/2): ")

                        if student_choice == '1':
                            student.show_student_info()
                        elif student_choice == '2':
                            break
                        else:
                            print("Invalid choice!")
                    break
            else:
                print("Student not found.")

        elif choice == '4':
            print("EXIT.")
            break

        else:
            print("Invalid choice, please try again.")

university = University("PIAIC")
uni()