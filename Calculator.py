first = int(input("Enter the first number : "))
operator = input("Enter operator (+,-,*,/,%) : ")
second = int(input("Enter the second number : "))
if operator == "+":
    print(first + second)
elif  operator == "-":
    print(first - second)
elif operator == "*":
    print(first * second)
elif operator == "/":
    print(first / second)
elif operator == "%":
    print(first % second)
else:
    print("Invalid Operation")