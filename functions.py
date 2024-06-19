# Inbuilt Functions.
y = max(313, 9874, 11, 234)
print(y)

x = min(312, 9874, 11, 234)
print("The minimum value is", x)

z = pow(2, 3)
print(z)

# User-defined function
def student():
    print("Hello")


student()  # Calling a function.

def person():
    print("Person is walking.")


person()

# Parameters and Arguments.
def add(num1, num2):
    print(num1 + num2)


add(109, 87)

def employee(fullname, age, email, maritalstatus, position):
    print(fullname, age, email, maritalstatus, position)


employee("John", 30, "johnte71@gmail.com", "Married", "Manager")
employee("Maspeda", 23, "maspeda7@gmail.com", "Single", "Director")
employee("Kutty", 30, "kutty8@gmail.com", "Married", "Coach")
employee("Claro", 30, "claro12@gmail.com", "Married", "CFO")
employee("Kaleb", 18, "caleb1@gmail.com", "Married", "Student")


