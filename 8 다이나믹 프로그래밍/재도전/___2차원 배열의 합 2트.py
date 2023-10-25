n,m = map(int,input().split())
l = [[0]*(m+1) for _ in range(n+1)]
for i in range(1,n+1):
    l[i][1:] = list(map(int,input().split()))
    
d = [[0]*(m+1) for _ in range(n+1)]

for i in range(1,n+1):
    for j in range(1,m+1):
        d[i][j] = d[i-1][j]+d[i][j-1]-d[i-1][j-1]+l[i][j]
print(*d,sep='\n')

# ⬇️ 다시!
for _ in range(int(input())):
    a,b,x,y = map(int,input().split())
    # 이게 아니라
    # 예시가 23이어서 그렇지 (우연이었음...^^)
    res = d[x][y]+d[a-1][b-1]-d[x-a][y]-d[x][y-b]
    # 얘래
    # 52였으면 3번째로 가는데 사실 1번째로 가야 맞으니까 바로 윗부분!
    # 아이디어는 맞았으니까 ㅇㅋ~ 마지막으로 한 번만 더 풀어보자~!
    res = d[x][y]+d[a-1][b-1]-d[a-1][y]-d[x][b-1]
    print(res)