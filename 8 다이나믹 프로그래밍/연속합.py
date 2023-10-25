n = int(input())
l = list(map(int,input().split()))

d = [l[0]]

for i in range(1,n):
    s = max(l[i],d[i-1]+l[i])
    d.append(s)

print(max(d))