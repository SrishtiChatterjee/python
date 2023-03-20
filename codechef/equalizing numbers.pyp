for i in range(int(input())):
    A,B=map(int,input().split())
    count = 0
    for d in range (1000):
        if((A+d) == (B-d)):
            count+=1
            break
        elif((B+d) == (A-d)):
            count+=1
            break
    if(count == 1): print ("Yes")
    else : print("No")
    
