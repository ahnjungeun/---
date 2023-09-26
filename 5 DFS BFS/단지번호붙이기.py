n = int(input())

G = [list(map(int,input())) for _ in range(n)]

from collections import deque

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(x,y):
    if G[x][y]:
        queue = deque([(x,y)])
        G[x][y] = 0
        c=0
        while queue:
            c+=1
            x,y = queue.popleft()
            for i in range(4):
                nx = x+dx[i]
                ny = y+dy[i]

                if 0<=nx<n and 0<=ny<n:
                    if G[nx][ny]:
                        queue.append((nx,ny))
                        G[nx][ny] = 0
        return c
    return 0

l = []
c=0
for i in range(n):
    for j in range(n):
        res = bfs(i,j)
        if res:
            l.append(res)
            c+=1
print(c,*sorted(l),sep='\n')