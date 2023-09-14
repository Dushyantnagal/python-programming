name1=input()
name2=input()
ch1=input()
ch2=input()
if (ch1=="Rock" and ch2=="Paper") or (ch1=="Paper" and ch2=="Scissor") or (ch1=="Scissor" and ch2=="Rock"):
    print(name2,"Win")
else:
    print(name1,"Win")
