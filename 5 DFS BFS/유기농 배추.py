import sys
sys.setrecursionlimit(10000)
# 아 무슨 재귀깊이를 내가 어떻게 알아요
# 무턱대고 큰 수로 바꾸면 되나???
# 차라리 bfs로 구현할게요 :(

def dfs(x,y):
    if 0<=x<n and 0<=y<m:
        if G[x][y]:
            G[x][y] = 0
            dfs(x-1,y)
            dfs(x+1,y)
            dfs(x,y-1)
            dfs(x,y+1)
            return True
    return False

from collections import deque

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(x,y):
    if G[x][y]:
        queue = deque([(x,y)])
        while queue:
            x,y = queue.popleft()
            for i in range(4):
                nx = x+dx[i]
                ny = y+dy[i]

                if 0<=nx<n and 0<=ny<m:
                    if G[nx][ny]:
                        G[nx][ny] = 0
                        queue.append((nx,ny))
        return True
    return False


for _ in range(int(input())):
    n,m,k = map(int,input().split())
    G = [[0]*m for _ in range(n)]

    for _ in range(k):
        a,b = map(int,input().split())
        G[a][b] = 1

    c=0
    for i in range(n):
        for j in range(m):
            if bfs(i,j):
                c+=1
    print(c)