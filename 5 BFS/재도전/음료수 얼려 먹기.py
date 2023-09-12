a,b = map(int,input().split())
G = []
for _ in range(a):
    G.append(list(map(int,input())))

x,y = 0,0

def dfs(x,y):
    if x<0 or x>=a or y<0 or y>=b:
        return False
    
    # 주어진 그래프 그대로 이용
    # marked 리스트 안 쓰고 하나 봐
    # 현재 위치가 0(미방문)이면
    if G[x][y] == 0:
        # 방문처리 하고
        G[x][y] = 1
        # 상하좌우 dfs 재귀호출
        dfs(x-1,y)
        dfs(x+1,y)
        dfs(x,y-1)
        dfs(x,y+1)
        # 반환은 하는데 값 저장을 안 해서 크게 의미는 없음
        # 해당 함수를 계속 타고 들어가다가 다 돌고 마지막에
        # 이 밑의 true 반환하면 아래 if문에서 카운트하는 것
        # 돌면서 연결되어있는 0인 곳 방문하면서 1로 변경하기에 for로 하나하나 탐색할 때
        # 바로 False로 반환돼서 카운트 안 됨
        # 연결된 곳 다 돌고 그때 마지막 최종으로 딱 한 번 True 반환하니까 카운트 가능
        return True
    return False

c = 0
for i in range(a):
    for j in range(b):
        if dfs(i,j):
            c+=1

print(c)

# 이해는 했는데... 다른 문제는 과연...