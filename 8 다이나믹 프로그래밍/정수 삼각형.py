l = []
n=int(input())
for _ in range(n):
    l.append(list(map(int,input().split())))
# print(l)

d = [[0]*i for i in range(1,n+1)]
# print(d)

for i in range(n):
    for j in range(len(l[i])):
        if j==0:
            s = l[i][j] + d[i-1][j]
        elif j==len(l[i])-1:
            s = l[i][j] + d[i-1][j-1]
        else:
            s = l[i][j] + max(d[i-1][j-1],d[i-1][j])
        d[i][j] = s

print(max(d[-1]))