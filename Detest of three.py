a =[0]
for i in a:
    if a[i]<=999:
     b=a[i]+1
     a.append(b)
    else:
       break


c=[]
for j in a:
    d = str(j)
    ld=d[-1]
    if (j %3!=0) and (ld!='3'):
       c.append(j)
n=int(input())
if c[n]!= c[-1]:
    print(c[n-1])
else:
    print(c(n))
