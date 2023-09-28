n,m,k = map(int,input().split())
G = [[0]*m for _ in range(n)]

for _ in range(k):
    x1,y1,x2,y2 = map(int,input().split())
    a = x2-x1
    b = y2-y1
    for i in range(y1,y1+b):
        for j in range(x1,x1+a):
            G[i][j] = 1

from collections import deque

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(x,y):
    if not G[x][y]:
        queue = deque([(x,y)])
        G[x][y] = 2
        c=1
        while queue:
            x,y = queue.popleft()
            for i in range(4):
                nx = x+dx[i]
                ny = y+dy[i]

                if 0<=nx<n and 0<=ny<m:
                    if not G[nx][ny]:
                        queue.append((nx,ny))
                        G[nx][ny] = 2
                        c+=1
        return c
    return 0
    
res=[]
for i in range(n):
    for j in range(m):
        c=bfs(i,j)
        if c:
            res.append(c)
print(len(res))
print(*sorted(res))