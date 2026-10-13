class Student :
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def afficher_infos(self):
        print(f"Nom: {self.name} - Age: {self.age}")


student1 = Student("Alice", 20)
student2 = Student("Marc", 24)
student3 = Student("Sarah", 19)

student1.afficher_infos()  # Output: Nom: Alice - Age: 20
student2.afficher_infos()  # Output: Nom: Marc - Age: 24
student3.afficher_infos()  # Output: Nom: Sarah - Age: 19


# print(student1.name)  # Output: Alice
# print(student1.age)   # Output: 20    