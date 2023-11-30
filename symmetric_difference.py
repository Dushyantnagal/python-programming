def symmetric_difference(arr1,arr2):
    ar=arr1 + arr2
    x=[]
    for i in ar:
        if ar.count(i)==1:
            x.append
    x.sort()
    return x

# main code 
ls1 = [3,5,67,7,2,4,3]
ls2 = [1,2,3,4,5]
re = symmetric_difference(ls1,ls2)
print(re)   