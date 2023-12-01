ls=[12,34,[45,8]]
dt= eval(str(ls))

dt[2].clear()
print(dt)
print(ls)
'''
ls={1:'one',2:'two',3:['three','THREE']}
 

dt[3].clear()
print(dt)
print(ls)
'''
# python dictionary clear()  :-  removes all items 
# python dictionary copy()  :-   returns shallow copy of a dictionary
# python dictionary fromkeys()  :-   creates dictionary from sequence 
# python dictionary get()  :-    returns the value of keys 
# python dictionary items()  :-   returns views od dictionary (key, value)pair
# python dictionary popitems()  :- returns& removes elements from dictionary
# python dictionary setdefault()  :- insert key with value if key is not present
# python dictionary pop()  :-    remove & returns elements having given key
# python dictionary values()  :- returns views of all values in dictionary
# python dictionary update()  :- updates the dictionary 