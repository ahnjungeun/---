n = int(input())
l = sorted(map(int,input().split()))
input()
f = list(map(int,input().split()))

for i in f:
    s,e=0,n-1
    while s<=e:
        m = (s+e)//2
        if l[m]==i:
            print(1)
            break
        elif l[m]>i:
            e = m-1
        else:
            s = m+1
    if s>e:
        print(0)