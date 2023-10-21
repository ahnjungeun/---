# 2차원 토마토
m,n = map(int,input().split())
g = [list(map(int,input().split())) for _ in range(n)]

l=[]

for i in range(n):
    for j in range(m):
        if g[i][j]==1:
            l.append((i,j))


from collections import deque
dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(l):
    queue = deque(l)
    # print(queue)
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]

            if 0<=nx<n and 0<=ny<m and g[nx][ny]==0:
                queue.append((nx,ny))
                g[nx][ny] = g[x][y]+1
                # print(*g,sep='\n')
                # print()

bfs(l)
res=1
for i in range(n):
    for j in range(m):
        if g[i][j]==0:
            print(-1)
            exit()
        else:
            res = max(g[i][j],res)

print(res-1)

# 90%에서 틀렸습니다?!?
# 반례!!
# 2 2
# 0 0
# 0 0
# 토마토가 하나 이상 있는 경우만 입력으로 주어진다.
# 익은 토마토라고는 말 안 했다 ^^ㅗ
# https://www.acmicpc.net/board/view/113000
# 이러면 deepcopy 필요없지~ 수정수정~