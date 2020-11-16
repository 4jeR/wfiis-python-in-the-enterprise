# Class diary
#
# Create program for handling lesson scores.
# Use python to handle student (highscool) class scores, and attendance.
# Make it possible to:
# - Get students total average score (average across classes)
# - get students average score in class
# - hold students name and surname
# - Count total attendance of student
#
# Please, use your imagination and create more functionalities.
# Your project should be able to handle entire school(s?).
# If you have enough courage and time, try storing (reading/writing)
# data in text files (YAML, JSON).
# If you have even more courage, try implementing user interface (might be text-like).
#
#Try to expand your implementation as best as you can. 
#Think of as many features as you can, and try implementing them.
#Make intelligent use of pythons syntactic sugar (overloading, iterators, generators, etc)
#Most of all: CREATE GOOD, RELIABLE, READABLE CODE.
#The goal of this task is for you to SHOW YOUR BEST python programming skills.
#Impress everyone with your skills, show off with your code.
#
#Your program must be runnable with command "python task.py".
#Show some usecases of your library in the code (print some things)
#
#When you are done upload this code to your github repository. 
#
#Delete these comments before commit!
#Good luck.




class Student:
    def __init__(self, name, surname, grades=[]):
        self.name = name
        self.surname = surname
        self.school_name = 'No school.'
        self.subject = 'No subject'
        self.class_grade = 'No class grade.'
        self.grades = []
        for grade in grades:
            self.grades.append(grade)


    def __str__(self):
        return f'{self.name} {self.surname}, {self.school_name}. Studies {self.subject} on {self.class_grade} year. Grades: {self.grades}' 

    def calculate_average(self):
        try:
            return sum(self.grades) / len(self.grades)
        except:
            print("No grades.")

class Diary:
    def __init__(self, school_name, subject, class_grade):
        self.school_name = school_name
        self.subject = subject
        self.class_grade = class_grade
        self.students = []
        self._index = 0

    def __iter__(self):
       return self

    def __next__(self):
        if self._index >= len(self.students):
            raise StopIteration
        current = self._index
        self._index += 1    
        return self.students[current]

    def __str__(self):
        return f'Average score for class {self.subject} is : {self.calculate_average()}'

    def add_student(self, student):
        self.students.append(student)
        student.school_name = self.school_name
        student.subject = self.subject
        student.class_grade = self.class_grade


    def calculate_average(self):
        s = 0
        for student in self.students:
            s += student.calculate_average()

        s /= len(self.students)

        return s 


if __name__=='__main__':
    diary = Diary("AGH UST", "Maths", "1")
    students = [
        Student('Adam', 'Kowalski', [4, 3, 4, 2]),
        Student('Piotr', 'Nowak', [2, 2, 5, 5]),
        Student('Anna', 'Robak', [2, 2, 5, 5])
    ]
    
    for student in students:
        diary.add_student(student)

    diary.add_student(Student("Monika", "Jedrzejczak", [3, 3, 5]))

    for student in diary:
        print(f'Average of student in {diary.subject} {student.name} {student.surname} {student.calculate_average()}')
    
        
