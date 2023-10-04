from collections import deque
# 상하좌우 대각선...
dx = [-1,1,0,0,-1,-1,1,1]
dy = [0,0,-1,1,-1,1,-1,1]

def bfs(x,y):
    if G[x][y] == 1:
        queue = deque([(x,y)])
        G[x][y] = 0
        while queue:
            x,y = queue.popleft()
            for i in range(8):
                nx = x+dx[i]
                ny = y+dy[i]

                if 0<=nx<h and 0<=ny<w:
                    if G[nx][ny] == 1:
                        queue.append((nx,ny))
                        G[nx][ny] = 0
        return 1
    return 0

w,h = map(int,input().split())
while w and h:
    G = [list(map(int,input().split())) for _ in range(h)]
    c = 0
    for i in range(h):
        for j in range(w):
            if bfs(i,j):
                c+=1
    print(c)
    w,h = map(int,input().split())