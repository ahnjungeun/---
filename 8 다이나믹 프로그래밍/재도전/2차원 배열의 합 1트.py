n,m = map(int,input().split())
l = [list(map(int,input().split())) for _ in range(n)]
    
d = [[0]*(m+1) for _ in range(n+1)]
k=0
pre=0
for i in range(1,n+1):
    for j in range(1,m+1):
        d[i][j] = pre+l[i-1][j-1]
        pre=d[i][j]
        k+=1


print(*d,sep='\n')
for _ in range(int(input())):
    a,b,x,y = map(int,input().split())
    print(d[x][y],d[a][b],l[a-1][b-1])
    print(d[x][y]-d[a][b]+l[a-1][b-1])

# 아 이거 문제 이해를 못함 다시!