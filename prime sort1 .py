def prime(num):
    num = int(num)
    if num <= 1:
        return '9'
    for i in range(2, num):
        if num % i == 0:
            return '9'
    else:
        return str(num)
    
st = input()[1:-1]
re = sorted(st, key=prime)
re = ''.join(re)
print(f'"{re}"')
