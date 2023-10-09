n=int(input())
lst= list(map(int, input().split()))

for i in lst:
    print(i%2, end=' ')