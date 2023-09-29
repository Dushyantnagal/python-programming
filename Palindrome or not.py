n=int(input('Enter the digits'))
cp=n
s=0
while n !=0:
    r=n%10
    s=s*10+r
    n=n//10
print('Reverse of',cp,'is',s)

if cp==s:
    print('Palindrome number')
else:
    print('Not a Palindrome number')
