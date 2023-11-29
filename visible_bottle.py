def visible_bottle(ls):
    f_list = []
    for i in ls:
        f_list.append(ls.count(i))
    return max(f_list)
    # return ls.count(max(ls, key=ls.count)) { it can be use also besides of this code }

#main code 
ls = [3,5,67,7,2,4,3]
re = visible_bottle(ls)
print(re)