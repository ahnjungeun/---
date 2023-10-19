n,m = map(int,input().split())
g = [list(input())for _ in range(n)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]

c=0

arr=set(g[0][0])

def dfs(x,y,k):
    global c
    print('c,k',c,k)
    c = max(c,k)
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]

        if 0<=nx<n and 0<=ny<m and g[nx][ny] not in arr:
            arr.add(g[nx][ny])
            # print(arr,k)
            # c=max(c,len(arr))
            dfs(nx,ny,k+1)
            arr.remove(g[nx][ny])

dfs(0,0,1)
print(c)