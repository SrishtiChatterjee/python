for i in range(int(input())):
    s=list(input())
    t=list(input())
    m=''
    for i in range (5):
        if t[i]==s[i]:
            m=m+'G'
        else: m=m+'B'
    print (m)
