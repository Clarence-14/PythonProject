
first = float(input("Enter first value: "))
op = input("Enter an operator (+, -, *, /): ")
second = float(input("Enter second value: "))

if op == '+':
    print(first + second)
elif op == '-':
    print(first - second)
elif op == '*':
    print(first * second)
elif op == '/':
    if second == 0:
        print("Math Error!")
    else:
        print(first / second)
else:
    print("Invalid operator input.")


