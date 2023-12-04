# given a  string  of lower case letter reduce by remove the chr. which  apperars more than  k times in string
# ex:- geeksforgeeks  k=2
st="geeksforgeeks"
k=2
d={}
for i in st:
    if i in d:
        d[i]=d[i]+1
    else:
        d[i]=i
for i in st:
    if (d[i]<k):
        ans=i
        print(ans)
