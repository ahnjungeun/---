n,m = map(int,input().split())
g = [list(map(int,input().split()))for _ in range(n)]
v = [[0]*m for _ in range(n)]

x,y=0,0

for i in range(n):
    for j in range(m):
        if g[i][j] == 2:
            x,y=i,j
            g[i][j]=0

from collections import deque
dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(x,y):
    queue = deque([(x,y)])
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]

            if 0<=nx<n and 0<=ny<m and g[nx][ny]==1 and not v[nx][ny]:
                queue.append((nx,ny))
                g[nx][ny] = g[x][y]+1
                v[nx][ny] = 1

bfs(x,y)
for i in range(n):
    for j in range(m):
        if v[i][j] and g[i][j]:
            print(g[i][j],end=' ')
        elif not v[i][j] and g[i][j]==1:
            print(-1,end=' ')
        else:
            print(0,end=' ')
    print()