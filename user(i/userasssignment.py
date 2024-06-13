# A simple python program that returns the smallest number from four.

first = int(input("Enter your first number: "))
second = int(input("Enter your second number: "))
third = int(input("Enter your third number: "))
fourth = int(input("Enter your fourth number: "))

if first < second and first < third and first < fourth:
    print(first, "is the smallest number.")

elif second < first and second < third and second < fourth:
    print(second, "is the smallest number.")

elif third < first and third < second and third < fourth:
    print(third, "is the smallest number.")

else:
    print(fourth, "is the smallest number.")


