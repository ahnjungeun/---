import copy

n,m = map(int,input().split())
G = [list(map(int,input().split())) for _ in range(n)]

from collections import deque

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(G,x,y):
    if G[x][y]:
        queue = deque([(x,y)])
        G[x][y] = 0
        while queue:
            x,y = queue.popleft()
            for i in range(4):
                nx = x+dx[i]
                ny = y+dy[i]
                if 0<=nx<n and 0<=ny<m and G[nx][ny]>0:
                    G[nx][ny] = 0
                    queue.append((nx,ny))
        return 1

fin = 0

while 1:
    G2 = copy.deepcopy(G)

    for i in range(n):
        for j in range(m):
            if G[i][j]:
                tmp = 0
                for k in range(4):
                    nx = i+dx[k]
                    ny = j+dy[k]

                    if 0<=nx<n and 0<=ny<m and G[nx][ny]==0:
                        tmp+=1
                new = G[i][j]-tmp
                G2[i][j] = new if new>0 else 0
    
    if G!=G2:
        fin+=1
    else:
        print(fin)
        break

    # print('G2')            
    # print(*G2,sep='\n')

    G = copy.deepcopy(G2)

    c=0
    for i in range(n):
        for j in range(m):
            if bfs(G2,i,j):
                c+=1
    
    
    if c==1:
        continue
    elif c==0:
        print(0)
        break
    else:
        print(fin)
        break




# 7 9
# 0 0 0 0 0 0 0 0 0
# 0 9 5 5 5 5 5 9 0
# 0 5 9 5 5 5 9 5 0
# 0 5 5 9 1 9 5 5 0
# 0 5 9 5 5 5 9 5 0
# 0 9 5 5 5 5 5 9 0
# 0 0 0 0 0 0 0 0 0

# 답 11

# 5 7
# 0 0 0 0 0 0 0
# 0 2 4 5 3 0 0
# 0 3 0 2 5 2 0
# 0 7 6 2 4 0 0
# 0 0 0 0 0 0 0

# 답 2

# 4 4
# 0 0 0 0
# 0 3 1 0
# 0 1 3 0
# 0 0 0 0

# 답 1

# 7 7
# 0 0 0 0 0 0 0
# 0 1 1 0 1 1 0
# 0 1 9 1 9 1 0
# 0 1 1 1 1 1 0
# 0 1 1 1 1 1 0
# 0 0 1 1 1 0 0
# 0 0 0 0 0 0 0

# 답 2

# 2 2
# 1 0
# 0 0

# 답 0?