n=input()
for i in n :
    a=n.count(i)
    if a==1:
        print(i)
        break
else:
        print('None')