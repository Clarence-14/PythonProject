class Student:
    def __init__(self, firstname, course, language):
        self.firstname = firstname
        self.course = course
        self.language = language

    def sleep(self):
        print(self.firstname, "is sleeping.")

c = Student("Caleb", "MIT", "Python")
print(c.firstname)
print(c.course)
print(c.language)
c.sleep()

student2 = Student("Clarence", "Web", "Ruby")
print(student2.firstname)
print(student2.course)
print(student2.language)
