T=int(input())
for i in range(T):
    
    l,r=list(map(int,input().split()))
    c=sum(j*(r//j) for j in range(1,r+1,2))
    d=sum(j*((l-1)//j) for j in range(1,l,2))
    print(c-d)
