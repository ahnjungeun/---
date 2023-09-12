# 보드크기
N = int(input())+1
# N이 6*6인데 좌표는 문제에서 (1,1)로 시작하기로 했으니 +1을 해주는 게 맞다

# 사과 개수
k = int(input())

# 사과 위치 기록
M = [[0]*N for _ in range(N)]
# 사과 위치 : 행 열
for _ in range(k):
    a,b = map(int,input().split())
    M[a][b] = 1

# 뱀의 방향 전환 횟수
l = int(input())
# 뱀 방향 전환 정보
B = [list(input().split()) for _ in range(l)]
# 현재까지 방향 전환한 횟수
i = 0

# 뱀 머리 위치
x,y = 1,1
# 뱀 꼬리 위치
# tx, ty = 1,1
M[x][y] = 2
# 꼬리 좌표보다 뱀이 있는 곳을 2로 바꿀 것
# 뱀.. ㄱ ㄴ ㄹ 이런 모양으로 움직이더라... 하하
# 나는 그냥 아예 몸을 직선으로 돌려버리는 줄

# 뱀이 차지하고 있는 칸을 저장하는 큐
# append() 하는 건 머리좌표! pop(0)해서 꼬리 제거
Q = [(x,y)]

direction = 0 # 또는 3으로 # <-아님
# 현재 바라보는 방향을 0(동쪽)이라고 설정하고 돌 때 +-1씩 하기

# 이동방향
# 상하좌우
dx = [0,1,0,-1]
dy = [1,0,-1,0]
# 상하좌우가 아닌 동남서북 방향으로 돌기! 늘 (반)시계방향으로 돌게 좌표 정렬


# 시간 세기
time = 0

# 돌기
# def turn():
#     global direction 
#     direction = 1 if direction==3 else 3
#     print('turn')
#     return
# 아 이게 L,D가 아니라 도는 거였구나
# DDD 시계방향 LLL 반시계방향으로 도는 것
def turn(d):
    global direction
    if d == 'L':
        direction = (direction-1)%4
    else:
        direction = (direction+1)%4
    print('turn')


# 시작
while 1:
  # 머리 이동하기
    print(time)
    nx = x + dx[direction]
    ny = y + dy[direction]

    # ntx = tx
    # nty = ty
    # 꼬리 위치는 이렇게 하는 게 아닌가봐

    # i=0
    # if time == int(B[i][0]):
    #     turn()
    #     i+=1
    # 이게 여기가 아닌가?

    # 뱀이 범위 안이면
    if 0<nx<N and 0<ny<N and M[nx][ny] != 2:
    # 범위 안인지 아닌지는 nx ny로 판별함
    # 이게 맞아야 x y로 갱신하는 것
    # 꼬리 삭제하는 대신 뱀의 좌표를 따로 설정할 것임

        # x = nx
        # y = ny
        # 갱신은 늘 마지막에!

        # 이동할 칸에 사과가 없으면
        if M[nx][ny] == 0:
        # 모든 기준은 nx ny로! 이게 다 통과되고 나서야 x y 갱신
            # ntx = tx + dx[direction]
            # nty = ty + dy[direction]
            # 꼬리 수정 대신
            M[nx][ny] = 2
            # 뱀이 차지하는 칸 추가하기
            Q.append((nx,ny))
            # 마지막 꼬리 좌표를 큐에서 삭제하고
            px,py = Q.pop(0)
            # 맵에서 뱀 위치정보 삭제
            M[px][py] = 0

        # 이동할 칸에 사과가 있으면
        elif M[nx][ny] == 1:
            # 뱀 머리부분 공간차지 2로 변경
            M[nx][ny] = 2
            # 차지한 칸 좌표 추가
            Q.append((nx,ny))


        # time += 1
        # 이동 자체는 독립적인 거라서 모든 조건 밖에
        # 범위 안에서만 시간이 지난 게 아니라 부딪혀서 지난 것도 포함해야 함
        # 좌표갱신도 조건문 밖에서! 
        # 만약 아니라면 밑에 else에서 break 걸려 갱신 안 됨

    else:
        time += 1
        # 부딪힌 시간도 체크하기
        # else 걸리면 밑에 time += 1 못 하고 반복 탈출
        break

    time += 1
    x,y = nx,ny

    # i=0
    # i를 밖에 빼줘야 하네.. 반복 돌 때마다 0으로 초기화되니까...ㅎㅎ;
    if i<l and time == int(B[i][0]):
        # i<l 조건이 필요한 이유 : B[마지막 i][0]에서 계속 조건 통과해 turn() 수행함
        turn(B[i][1])
        i+=1
    

print('답 :',time)


# -------- 노트 --------

# 채점 돌릴 때 프린트문 수정해서 돌리기