class Classroom:
    def __init__(self, name):
        self.name = name
        self.students = []
        self.assignments = []

    def add_student(self, student):
        self.students.append(student)

    def students_list(self):
        return [student.name for student in self.students]

    def create_assignment(self, assignment):
        self.assignments.append(assignment)

    def assignments_list(self):
        return [assignment.name for assignment in self.assignments]

    def __str__(self):
        return f"Classroom {self.name}"

class Student:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def __str__(self):
        return f"Student {self.name}"

class Assignment:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Assignment {self.name}"

class VirtualClassroomManager:
    def __init__(self):
        self.classrooms = {}
        self.students = {}

    def add_classroom(self, name):
        if name in self.classrooms:
            print(f"Classroom {name} already exists.")
        else:
            classroom = Classroom(name)
            self.classrooms[name] = classroom
            print(f"Classroom {name} has been created.")

    def add_student(self, id, classroom_name):
        if classroom_name not in self.classrooms:
            print(f"Classroom {classroom_name} does not exist.")
        elif id in self.students:
            print(f"Student {id} already exists.")
        else:
            student = Student(id, id)
            self.students[id] = student
            self.classrooms[classroom_name].add_student(student)
            print(f"Student {id} has been enrolled in {classroom_name}.")

    def create_assignment(self, classroom_name, assignment_name):
        if classroom_name not in self.classrooms:
            print(f"Classroom {classroom_name} does not exist.")
        else:
            assignment = Assignment(assignment_name)
            self.classrooms[classroom_name].create_assignment(assignment)
            print(f"Assignment for {classroom_name} has been scheduled.")

    def list_students_in_class(self, classroom_name):
        if classroom_name not in self.classrooms:
            print(f"Classroom {classroom_name} does not exist.")
        else:
            students = self.classrooms[classroom_name].students_list()
            if students:
                print(f"Students in {classroom_name}: {', '.join(students)}")
            else:
                print(f"No students in {classroom_name}.")

    def list_assignments_in_class(self, classroom_name):
        if classroom_name not in self.classrooms:
            print(f"Classroom {classroom_name} does not exist.")
        else:
            assignments = self.classrooms[classroom_name].assignments_list()
            if assignments:
                print(f"Assignments in {classroom_name}: {', '.join(assignments)}")
            else:
                print(f"No assignments in {classroom_name}.")

    def submit_assignment(self, student_id, classroom_name, assignment_name):
        if student_id not in self.students:
            print(f"Student {student_id} does not exist.")
        elif classroom_name not in self.classrooms:
            print(f"Classroom {classroom_name} does not exist.")
        else:
            assignment = next((a for a in self.classrooms[classroom_name].assignments if a.name == assignment_name), None)
            if assignment:
                print(f"Assignment submitted by Student {student_id} in {classroom_name}.")
            else:
                print(f"Assignment {assignment_name} not found in {classroom_name}.")

if __name__ == "__main__":
    manager = VirtualClassroomManager()

    while True:
        print("\nVirtual Classroom Manager")
        print("1. Add Classroom")
        print("2. Add Student")
        print("3. Schedule Assignment")
        print("4. List Students in Classroom")
        print("5. List Assignments in Classroom")
        print("6. Submit Assignment")
        print("7. Exit")

        choice = input("Enter your choice: ")
        match choice:
            case "1":
                name = input("Enter Classroom Name: ")
                manager.add_classroom(name)

            case "2":
                id = input("Enter Student ID: ")
                classroom_name = input("Enter Classroom Name: ")
                manager.add_student(id, classroom_name)

            case "3":
                classroom_name = input("Enter Classroom Name: ")
                assignment_name = input("Enter Assignment Name: ")
                manager.create_assignment(classroom_name, assignment_name)

            case "4":
                classroom_name = input("Enter Classroom Name: ")
                manager.list_students_in_class(classroom_name)

            case "5":
                classroom_name = input("Enter Classroom Name: ")
                manager.list_assignments_in_class(classroom_name)

            case "6":
                student_id = input("Enter Student ID: ")
                classroom_name = input("Enter Classroom Name: ")
                assignment_name = input("Enter Assignment Name: ")
                manager.submit_assignment(student_id, classroom_name, assignment_name)

            case "7":
                print("Exiting Virtual Classroom Manager")
                break

            case _:
                print("Invalid choice. Please try again.")
