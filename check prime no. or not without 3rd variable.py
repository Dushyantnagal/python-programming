def is_prime(num):
    if num < 2:
        return False
    if num == 2:
        return True
    
    i = 2
    while i * i <= num:
        if num % i == 0:
            return False
        i += 1
    return True



number = int(input("Enter a number: "))
if is_prime(number):
    print(f"{number} is a prime number.")
else:
    print(f"{number} is not a prime number.")
