n=int(input())
g = [list(input()) for _ in range(n)]
# 이야 난 여기 안 건들였는데 다른사람은
# 그래프를 2개 만들어서 replace('R','G')를 했구나
# 똑똑한 걸~

from collections import deque

marked = [[0]*n for _ in range(n)]
marked2 = [[0]*n for _ in range(n)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(marked,x,y):
    if not marked[x][y]:
        queue = deque([(x,y)])
        marked[x][y] = 1
        while queue:
            x,y = queue.pop()
            for i in range(4):
                nx = x+dx[i]
                ny = y+dy[i]

                if 0<=nx<n and 0<=ny<n and not marked[nx][ny]:
                    if g[x][y]==g[nx][ny]:
                        queue.append((nx,ny))
                        marked[nx][ny] = 1
        return 1

def bfs2(marked,x,y):
    if not marked[x][y]:
        queue = deque([(x,y)])
        marked[x][y] = 1
        while queue:
            x,y = queue.pop()
            for i in range(4):
                nx = x+dx[i]
                ny = y+dy[i]

                if 0<=nx<n and 0<=ny<n and not marked[nx][ny]:
                    if g[x][y]==g[nx][ny] or (g[x][y]=='R' and g[nx][ny]=='G') or (g[x][y]=='G' and g[nx][ny]=='R'):
                        queue.append((nx,ny))
                        marked[nx][ny] = 1
        return 1

a,b=0,0
for i in range(n):
    for j in range(n):
        if bfs(marked,i,j):
            a+=1
        if bfs2(marked2,i,j):
            b+=1
print(a,b)