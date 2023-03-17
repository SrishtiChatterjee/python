for i in range(int(input())):
    c = 0
    n = int(input())
    S = input()
    for i in range(n - 1):
        if S[i] == S[i+1]:
            c+=1
    print(c)
