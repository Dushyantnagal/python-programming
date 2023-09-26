n=int(input("enter no.:"))
if (n==0 or n==1):
    print("yes")
else:
    a=0
    b=1
    i=2
    while True:
        c=a+b
        a=b
        b=c
        i+=1
        if(c==n):
            print("yes")
            break
        elif (c>n):
            print("no")
            break