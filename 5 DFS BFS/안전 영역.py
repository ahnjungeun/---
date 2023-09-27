n = int(input())
G = [list(map(int,input().split()))for _ in range(n)]

from collections import deque

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(G,x,y,k):
    if G[x][y] > k:
        queue = deque([(x,y)])
        G[x][y] = k
        while queue:
            x,y = queue.popleft()
            
            for i in range(4):
                nx = x+dx[i]
                ny = y+dy[i]

                if 0<=nx<n and 0<=ny<n:
                    if G[nx][ny] > k:
                        queue.append((nx,ny))
                        G[nx][ny] = k
        return 1
    return 0

import copy
res = []
for k in range(101):
    c=0
    m=copy.deepcopy(G)
    for i in range(n):
        for j in range(n):
            if bfs(m,i,j,k):
                c+=1
    res.append(c)
print(max(res))