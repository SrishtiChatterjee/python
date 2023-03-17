t=int(input())
for x in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    count=0
    if a[0]!=a[1]:
        count+=1
    if a[-1]!=a[-2]:
        count+=1
    for i in range(1,n-1):
        if a[i]!=a[i-1] or a[i+1]!= a[i]:
            count+=1
    print(count)
