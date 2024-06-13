temperature = 25

if temperature > 25:
    print("It is hot.")
elif temperature < 25:
    print("It is cold.")

else:
    print("Normal Temperature.")

# A program that returns the largest number among three numbers.
first = 56
second = 23
third = 78

if first > second and first > third:
    print(first, "is the largest number.")

elif second > first and second > third:
    print(second, "is the largest number.")

else:
    print(third, "is the largest number.")

# A program that checks whether a number is even or odd
num = int(input("Enter a number: "))
if num == 0:
    print(num, "is Neutral.")
elif (num % 2) == 0:
    print(num, "is Even.")
else:
    print(num, "is Odd.")

# A python program that returns the area of a rectangle.
# A = L*W
length = int(input("Enter a length: "))
width = int(input("Enter a width: "))
area = length * width
print("The area is", area)

# A python program that returns the area of a trapezium.
# A = ½ (a + b) h
a = int(input("Enter a value: "))
b = int(input("Enter a value: "))
h = int(input("Enter a height: "))
Area = 0.5*(a + b)*h
print("The area is", Area)

