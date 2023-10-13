list1 = list(map(int, input("Enter the elements of the list: ").split()))
list2 = []
for i in list1:
    if i % 2 != 0:
        list2.append(i**2)
if len(list2) == 0:
    print("There are no odd numbers in the list")
else:
    print("Odd numbers in the list are", *list2)
