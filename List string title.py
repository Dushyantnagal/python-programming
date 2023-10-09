lst = eval(input())
new_lst= []
for i in lst:
    new_lst.append(i.istitle())
print(new_lst)