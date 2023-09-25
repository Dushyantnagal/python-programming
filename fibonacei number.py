n=int(input())
if (n==0 or n==1):
    print(n)
else:
    a=0
    b=1
    i=2
    while(i<=n):
        c=a+b
        a=b
        b=c
        i+=1
    print(c)