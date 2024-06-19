
try:
    number = 12
    print(number)
except:
    print("An error occurred.")

finally:
    print("Success")

x = 82
y = 0
try:
    print(x/y)
except:
    print("Arithmetic error occurred")
finally:
    print("Success")
