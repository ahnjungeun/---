# 보드크기
n = int(input())

# 사과 개수
k = int(input())

# 사과 위치 기록
M = [[0]*n for _ in range(n)]
# 사과 위치 : 행 열
for _ in range(k):
    a,b = map(int,input().split())
    M[a][b] = 1

# 뱀의 방향 전환 횟수
l = int(input())
# 뱀 방향 전환 정보
B = [list(input().split()) for _ in range(l)]

# 뱀 머리 위치
x,y = 1,1
# 뱀 꼬리 위치
tx, ty = 1,1

direction = 1 # 또는 3으로

# 이동방향
# 상하좌우
dx = [-1,1,0,0]
dy = [0,0,-1,1]

# 시간 세기
time = 0

# 돌기
def turn():
    global direction 
    direction = 1 if direction==3 else 3
    print('turn')
    return

# 시작
while 1:
  # 머리 이동하기
    print(time)
    nx = x + dx[direction]
    ny = y + dy[direction]

    ntx = tx
    nty = ty

    i=0
    if time == int(B[i][0]):
        turn()
        i+=1

    # 뱀이 범위 안이면
    if 0<x<n and 0<y<n and 0<ntx<n and 0<nty<n:
        x = nx
        y = ny

        # 이동할 칸에 사과가 없으면
        if M[x-1][y-1] == 0:
            ntx = tx + dx[direction]
            nty = ty + dy[direction]
        
        time += 1
        
    else:
        break
    

print('답 :',time)