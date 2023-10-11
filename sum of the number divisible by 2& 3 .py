n = int(input("Enter the value of n: "))
sum = 0
for i in range(1, n+1):
    if i % 2 == 0 and i % 3 == 0:
        sum += i
print("Sum of the numbers divisible by 2 and 3 upto n is", sum)