n = int(input())
l = sorted(map(int,input().split()))
m = int(input())
f = map(int,input().split())

def bin(a,t,s,e):
    while s<=e:
        m = (s+e)//2
        if a[m] == t:
            print(1,end=' ')
            return
        elif a[m] > t:
            e = m-1
        else:
            s = m+1
    print(0,end=' ')

for i in f:
    bin(l,i,0,n-1)


# 시간초과
for i in f:
    print(1 if i in l else 0,end=' ')
