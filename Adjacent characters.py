st=input()
if len(st)%2==0:
    a,b,x=0,1,""
    for i in range(int(len(st)/2)):
        x=x+st[b]+st[a]
        b=b+2
        a=a+2
    print(x)
else:
    print('Odd length.')