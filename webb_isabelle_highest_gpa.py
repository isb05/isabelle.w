"""
Created by Isabelle Webb. This program can add students to a course, find the student with the highest gpa, and print the
course size and information.
"""

#creating the class Student
class Student:
    def __init__(self, first, last, gpa):
        self.first = first
        self.last = last
        self.gpa = gpa
#stores gpa
    def get_gpa(self):
        return self.gpa
#stores first name
    def get_first(self):
        return self.first
#stores last name
    def get_last(self):
        return self.last
#creating class Course
class Course:
    def __init__(self):
        self.roster = []
        self.gpa = []
#appends student to roster list
    def add_student(self, student):
        self.roster.append(student)
        self.gpa.append(student.get_gpa())
#returns number of students in roster list
    def course_size(self):
        return len(self.roster)
#returns student with highest gpa
    def find_student_highest_gpa(self):
        if not self.gpa:
            print(f"\nCourse size: {course.course_size()}")
            #in case roster is empty
            raise ValueError('Course roster is empty.')
        #finds highest gpa
        else:
            highest_gpa = max(self.gpa)
            index_max_gpa = self.gpa.index(highest_gpa)
            top_student = self.roster[index_max_gpa]
            return highest_gpa, f"{top_student.get_first()} {top_student.get_last()}"

course = Course()
stop_list = ['q', 'quit']

#get students name
while True:
    print('Please add students to the course: (quit or q to exit).')
    first_name = input("Enter First name: ")
    if first_name in stop_list:
        break

    last_name = input("Enter Last name: ")

#get student gpa as numeric value
    try:
        gpa = float(input("Enter student's GPA: "))
        student = Student(first_name, last_name, gpa)
        course.add_student(student)

    except ValueError:
        print('\nException: Please enter GPA as a numeric value.')

#prints info about student with highest gpa
    try:
        highest_gpa, top_student = course.find_student_highest_gpa()
        print(f'Course size: {course.course_size()} students')
        print(f'Top student: {top_student} (GPA: {highest_gpa})')
    except ValueError as e:
        print(e)

    




    
