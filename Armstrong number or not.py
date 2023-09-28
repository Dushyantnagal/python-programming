n=int(input('Enter the digits'))
cp=n
pw=0
while n !=0:
   pw+=1
   n=n//10

s=0
n=cp
while n!=0:
   r=n%10
   s=s+r**pw
   n=n//10
if s==cp:
   print(cp, 'is armstrong number')
else:
   print(cp,'is not armstrong number')