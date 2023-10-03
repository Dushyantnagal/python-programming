st='hello world'
pt='ll'
val=0
for i in range (st.count(pt)):
    dn=st.index(pt,val)
    print(dn,end='')
    val=dn+1