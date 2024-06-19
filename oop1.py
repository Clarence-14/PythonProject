class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def details(self):
        print(self.name, "is studying.")


accountant = Person("Joe", 34, "Male")
print(accountant.name)
print(accountant.age)
print(accountant.gender)
accountant.details()
consultant = Person("Martha",  56, "Female")
print(consultant.gender)
print(consultant.age)
print(consultant.name)
doctor = Person("James", 27, "Male")
print(doctor.age)
print(doctor.name)
print(doctor.gender)
doctor.details()
