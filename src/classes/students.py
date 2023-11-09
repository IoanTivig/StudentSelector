class Student:
    def __init__(self, first_name, surname, assigned):
        self.first_name = first_name
        self.surname = surname
        self.assigned = assigned

    def get_full_name(self):
        return f"{self.first_name} {self.surname}"

    def get_assigned(self):
        return self.assigned


class Students:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def get_students(self):
        return self.students

    def get_student(self, index):
        return self.students[index]

    def get_student_by_name(self, name):
        for student in self.students:
            if student.get_full_name() == name:
                return student
        return None

    def get_student_by_assigned(self, assigned):
        for student in self.students:
            if student.get_assigned() == assigned:
                return student
        return None

    def get_student_by_index(self, index):
        return self.students[index]

    def get_student_count(self):
        return len(self.students)

    def remove_student_by_name(self, name):
        for student in self.students:
            if student.get_full_name() == name:
                self.students.remove(student)

    def remove_student_by_assigned(self, assigned):
        for student in self.students:
            if student.get_assigned() == assigned:
                self.students.remove(student)

    def remove_student_by_index(self, index):
        del self.students[index]