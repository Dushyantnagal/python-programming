def gcd(a, b):
    if a == 0:
        return b
    return gcd(b % a, a)
 
 
a = 2
b = 4
print(gcd(a, b))
