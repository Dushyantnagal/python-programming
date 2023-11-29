# w. a p. fuc. thta recieve a list of integers and return value 1 if of all integers are sorted in accending order -1 if list is unsorted and 0 if list is sorted in decending order
def sorted_or_not(ls):

    if lst==sorted(lst):
        return 1  
    elif lst==sorted(lst,reverse=True):
        return 0 
    else:
        return -1 

#main code
lst=[3,5,67,7]
re=sorted_or_not(lst)
print(re)