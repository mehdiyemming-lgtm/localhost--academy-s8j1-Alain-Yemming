class Student:
    def __init__(self, name):
        self.name = name
        self.grades = []
    def add_grade(self, grade):
        if grade >= 0 and grade <= 20:
            self.grades.append(grade)
        else:
            print("La note est inavalide")
    def average_grade(self):
        if len(self.grades) == 0:
            return 0
        return sum(self.grades) / len(self.grades)


student = Student("Samuel")
student.add_grade(14)
student.add_grade(18)
student.add_grade(12)  


print(student.grades)  # Output: [14, 18, 12]
print(f"Moyenne :{student.average_grade():.2f}")  # Output: Moyenne :14.67

student.add_grade(25)  # Output: La note est inavalide
student.add_grade(-5)  # Output: La note est inavalide
