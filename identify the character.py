st=input('Enter the string')
alp_lower=0
alp_upper=0
digits=0
space=0
special=0
for i in st:
    if 'a'<=i <='z':
        alp_lower+=1
    elif 'A'<=i <= 'Z':
        alp_upper +=1
    elif '0' <=i <= '9':
        digits+= 1
    elif i==" ":
        space+=1
    else:
        special+=1

print('Number of the alphabets lower case', alp_lower)
print('Number of the alphabets upper case', alp_upper)
print('Number of the digits case',digits)
print('Number of the space', space)
print('Number of the  special',  special)