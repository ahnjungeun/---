n,m = map(int,input().split())
G = [list(map(int,input())) for _ in range(n)]

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

            if 0<=nx<n and 0<=ny<m:
                if G[nx][ny]==1:
                    queue.append((nx,ny))
                    G[nx][ny] = G[x][y]+1

    return G[n-1][m-1]

print(bfs(0,0))