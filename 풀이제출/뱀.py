N = int(input())+1
k = int(input())

M = [[0]*N for _ in range(N)]
for _ in range(k):
    a,b = map(int,input().split())
    M[a][b] = 1

l = int(input())
B = [list(input().split()) for _ in range(l)]
i = 0

x,y = 1,1
M[x][y] = 2

Q = [(x,y)]

direction = 0

dx = [0,1,0,-1]
dy = [1,0,-1,0]

time = 0

def turn(d):
    global direction
    if d == 'L':
        direction = (direction-1)%4
    else:
        direction = (direction+1)%4

while 1:
    nx = x + dx[direction]
    ny = y + dy[direction]

    if 0<nx<N and 0<ny<N and M[nx][ny] != 2:
        if M[nx][ny] == 0:
            M[nx][ny] = 2
            Q.append((nx,ny))
            px,py = Q.pop(0)
            M[px][py] = 0

        elif M[nx][ny] == 1:
            M[nx][ny] = 2
            Q.append((nx,ny))

    else:
        time += 1
        break

    time += 1
    x,y = nx,ny

    if i<l and time == int(B[i][0]):
        turn(B[i][1])
        i+=1
    
print(time)