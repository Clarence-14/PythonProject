class Student:
    def __init__(self, firstname, course, language):
        self.firstname = firstname
        self.course = course
        self.language = language

    def __sleep(self):
        print(self.firstname, "is sleeping.")
    def sleep(self):
        return self.__sleep()

student2 = Student("Clarence", "Web", "Ruby")

