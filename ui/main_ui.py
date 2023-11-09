# ------------------------------------------------------
# ------------------ OpenDEP Control -------------------
# ------------------------------------------------------

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QDialog, QFileDialog
from PyQt5.uic import loadUi
import random

from ui.resources.graphical_resources import *  # don't remove this line
from src.classes.students import Students, Student

class MainUI(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        loadUi("ui/main.ui", self)
        self.setWindowTitle("OpenDEP Control")
        self.setWindowIcon(QIcon("icon.png"))

        self.students = Students()
        self.selected_student = None

        self.pyqt5_dynamic_button_load_list.clicked.connect(self.load_students)
        self.pyqt5_dynamic_button_random_student.clicked.connect(self.get_random_student)
        self.pyqt5_dynamic_button_assign_student.clicked.connect(self.assign_student)
        self.pyqt5_dynamic_list_students.itemClicked.connect(self.click_student_in_list)
        self.pyqt5_dynamic_add_to_selection_list.clicked.connect(self.move_student_to_selected_students)
        self.pyqt5_dynamic_button_remove_student.clicked.connect(self.remove_student_from_selected_list)
        self.pyqt5_dynamic_button_save_list.clicked.connect(self.save_students)
        self.pyqt5_dynamic_button_save_selected_list.clicked.connect(self.save_selected_students)

    def load_students(self):
        file_name = QFileDialog.getOpenFileName(self, "Open File", "C:\\", "CSV Files (*.csv)")
        with open(file_name[0], mode="r", encoding='utf-8') as file:
            skip_first = True
            for line in file:
                if skip_first:
                    skip_first = False
                    continue
                line = line.strip().split(",")
                student = Student(line[1], line[2], line[3])
                self.students.add_student(student)
        i = 0
        for student in self.students.get_students():
            self.pyqt5_dynamic_list_students.addItem(f"{i}.  {student.get_full_name()} - {student.get_assigned()}")
            i += 1

    def save_students(self):
        file_name = QFileDialog.getSaveFileName(self, "Save File", "C:\\", "CSV Files (*.csv)")
        with open(file_name[0], mode="w", encoding='utf-8') as file:
            file.write("No.,First Name,Surname,Assigned\n")
            i = 0
            for student in self.students.get_students():
                file.write(f"{i},{student.first_name},{student.surname},{student.assigned}\n")
                i += 1

    def save_selected_students(self):
        file_name = QFileDialog.getSaveFileName(self, "Save File", "C:\\", "CSV Files (*.csv)")
        with open(file_name[0], mode="w", encoding='utf-8') as file:
            file.write("Name\n")
            for i in range(self.pyqt5_dynamic_list_selected_students.count()):
                file.write(f"{self.pyqt5_dynamic_list_selected_students.item(i).text()}\n")

    def get_random_student(self):
        found = False
        while not found:
            random_student = self.students.get_students()[random.randint(0, self.students.get_student_count() - 1)]
            if random_student.assigned == "Yes":
                found = False
            else:
                found = True

        self.selected_student = random_student
        self.pyqt5_dynamic_label_student_name.setText(random_student.get_full_name())
        self.pyqt5_dynamic_list_students.setCurrentRow(self.students.get_students().index(random_student))

    def assign_student(self):
        self.selected_student.assigned = "Yes"
        self.pyqt5_dynamic_list_students.clear()
        i = 0
        for student in self.students.get_students():
            self.pyqt5_dynamic_list_students.addItem(f"{i}.  {student.get_full_name()} - {student.get_assigned()}")
            i += 1

    def click_student_in_list(self):
        index = self.pyqt5_dynamic_list_students.currentRow()
        self.selected_student = self.students.get_student_by_index(index)
        self.pyqt5_dynamic_label_student_name.setText(self.students.get_student_by_index(index).get_full_name())

    def move_student_to_selected_students(self):
        item = self.selected_student.get_full_name()
        self.pyqt5_dynamic_list_selected_students.addItem(item)
        self.pyqt5_dynamic_label_no_of_selected_students.setText(str(self.pyqt5_dynamic_list_selected_students.count()))

    def remove_student_from_selected_list(self):
        item = self.pyqt5_dynamic_list_selected_students.currentItem()
        self.pyqt5_dynamic_list_selected_students.takeItem(self.pyqt5_dynamic_list_selected_students.row(item))
        self.pyqt5_dynamic_label_no_of_selected_students.setText(str(self.pyqt5_dynamic_list_selected_students.count()))

