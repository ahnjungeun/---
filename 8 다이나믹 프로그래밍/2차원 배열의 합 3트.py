n,m = map(int,input().split())
l = [[0]*(m+1) for _ in range(n+1)]
for i in range(1,n+1):
    l[i][1:]=list(map(int,input().split()))

d = [[0]*(m+1) for _ in range(n+1)]  

for i in range(1,n+1):
    for j in range(1,m+1):
        d[i][j] = d[i-1][j]+d[i][j-1]-d[i-1][j-1]+l[i][j]

for _ in range(int(input())):
    a,b,x,y = map(int,input().split())
    ans = d[x][y]-d[x][b-1]-d[a-1][y]+d[a-1][b-1]
    print(ans)