dct = eval(input())
ls1 = []
ls2 = []

for i in dct:
    if dct[i] < 20 or dct[i] > 40:
        ls1.append(i)
    else:
        ls2.append(i)
ls1.sort()
ls2.sort()
print(f'''[
 {ls1},
 {ls2}
]''')