try:
    num1 = int(input("Enter number 1: "))
    num2 = int(input("Enter number 2: "))

except ValueError or TypeError as e:
    print(e)

print("This is importtant line")
