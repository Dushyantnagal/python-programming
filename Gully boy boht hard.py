st=input()
node=int(input())
rp=int(input())

data=st[node:] + st[:node]
data=data.replace(' ','')
define_data=data*rp
print(*define_data)