# 입력 받기
n,m = map(int,input().split())
x,y,direction = map(int,input().split())
# M : 바다 = 1 육지 = 0
M = [list(map(int,input().split())) for _ in range(n)]

# 방문 위치 저장 : 방문 = 1 미방문 = 0
d = [[0]*m for _ in range(n)]

# 현재 위치 방문 처리
d[x][y] = 1

# 북 동 서 남
dx = [-1,0,1,0]
dy = [0,1,0,-1]

# 왼쪽으로 돌기
# 문제에서 왼쪽방향으로 돌아서 움직임 (돈 방향의 앞쪽으로 못 가면 한 번 더 돌기)
def turn_left():
    # direction 북 = 0 동 = 1 남 = 2 서 = 3
    global direction
    # 도는 방향 순서 : 북 서 남 동
    # 돌면 1 빼줘서 지금 바라보는 방향 설정
    direction -=1
    # 북쪽(0)에서 한번 돌아서 1 빼주면 -1 됨. 이때 다음 순환인 서쪽으로 설정하기
    if direction == -1:
        direction = 3

# 시뮬레이션 시작
# 시작 시 처음 서 있는 곳 1칸 세기
count = 1

# 몇 번 돌았니? 4번 돌았다는 얘기는 갈 곳이 4방향 전부 없다는 뜻!
turn_time = 0
while 1:
    # 돌기
    turn_left()

    # 돈 다음에 좌표 이동할 좌표 설정하기
    # 설정하고 다음 갈 곳이 이동불가면 x,y를 갱신하지 않고 nx,ny로 남겨둠

    # 어느 방향으로 갈 거냐? 바로 현재 방향쪽으로 갈 거지~
    # +는 앞으로 이동 -는 뒤로 이동
    nx = x + dx[direction]
    ny = y + dy[direction]

    # 미방문 and 육지이면
    if d[nx][ny] == 0 and M[nx][ny] == 0:
        # 방문처리
        d[nx][ny] = 1
        # 방문했으니 현재 위치인 x y 갱신하기
        x = nx
        y = ny

        # 방문한 육지 수 갱신하기
        count+=1

        # 돌아서 성공적으로 다른 육지로 이동했으니 돈 횟수 초기화
        turn_time = 0

        # 다시 또 탐색시작
        continue
    
    # 회전한 후 앞에 있는 칸이 방문 or 바다
    else:
        turn_time+=1

    # 4방향 다 돌았는데도 못 움직인 경우
    if turn_time == 4:
        # 뒤로가기(백트래킹)
        # 현재 바라보는 방향에서 +는 앞으로 이동 -는 뒤로 이동
        nx = x - dx[direction]
        ny = y - dy[direction]

        # 뒤돌아서 갈 곳이 육지면
        if M[nx][ny] == 0:
            x = nx
            y = ny

        # 이게 끝까지 다 탐색하고 계속 뒤로가다보면 초기 위치에 도착함
        # 이 때 뒤돌아서 갈 곳이 바다면 반복탈출 -> 종료
        else:
            break
        
        # 다 돌고 뒤로 갈 곳이 있어 뒤로 갔으니 돈 횟수 초기화
        turn_time = 0
        

# 반복을 탈출했다는 것 = 갈 곳 다 가봤다는 뜻
# 몇 개의 육지를 방문했나 출력
print(count)