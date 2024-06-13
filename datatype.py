# Datatype

number = 60  # int
num = 45.36  # float
greeting = "Hello there."  # str
isPythonInteresting = True  # boolean
fruits = ["banana", "mango", "apple"]  # list
cars = ("BMW", "Mercedes-Benz", "Toyota", "Jeep")  # tuple
countries = {"Kenya", "Tanzania", "Uganda"}  # set
student = {
    "firstname": "Thierry",
    "age": 18,
    "course": "MIT",
    "nationality": "French"

}  # dictionary

print(num)
print(isPythonInteresting)
print(fruits)
print(cars)
print(countries)
print(student['firstname'])

# Determining datatype
print(type(isPythonInteresting))
print(type(cars))

# Typecasting is converting one datatype to another.
print(int(num))
print(float(number))
