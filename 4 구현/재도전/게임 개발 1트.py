n,m = map(int,input().split())
x,y,d = map(int,input().split())
G = []
for _ in range(n):
    G.append(list(map(int,input().split())))

M = [[0]*m for _ in range(n)]

# 북동남서
dx = [-1,0,1,0]
dy = [0,-1,0,1]

def turn(d):
    if d==0:
        d = 3
    else:
        d -= 1
    return d

c=0

#----
turn_count=0
#----

while 1:
    d = turn(d)

    nx = x+dx[d]
    ny = y+dy[d]

    #----
    if M[nx][ny]==0 and G[nx][ny]==0:
        M[nx][ny]=1
        x,y=nx,ny
        c+=1
        turn_count=0
        continue
    else:
        turn_count+=1

    if turn_count==4:
        nx = x-dx[d]
        ny = y-dy[d]
        if G[nx][ny]==0:
            x,y=nx,ny
        else:
            break
        turn_count=0
    #----
    
print(c)