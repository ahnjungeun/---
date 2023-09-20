# 음료수 얼려먹기
n,m = map(int,input().split())
G=[]
for _ in range(n):
    G.append(list(map(int,input())))

x,y=0,0

def dfs(x,y):
    if 0<=x<n and 0<=y<m:
        if G[x][y]:
            return False
        G[x][y] = 1
        dfs(x,y-1)
        dfs(x,y+1)
        dfs(x-1,y)
        dfs(x+1,y)
        return True
    return False

c=0

for i in range(n):
    for j in range(m):
        if dfs(i,j):
            # print(i,j)
            c+=1
print(c)


