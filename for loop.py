 
n = int(input("Enter the number of values you want to input: "))
total = 0
product = 1


for i in range(n):
    value = float(input(f"Enter value {i+1}: "))
    total += value
    product *= value


average = total / n


print(f"Product of the numbers: {product}")
print(f"Average of the numbers: {average}")
