n,m = map(int,input().split())
G = [list(input())for _ in range(n)]

arr=set()
k=0
def dfs(x,y):
    global k
    if 0<=x<n and 0<=y<m:
        if G[x][y] not in arr:
            arr.append(G[x][y])
            dfs(x-1,y)
            dfs(x+1,y)
            dfs(x,y-1)
            dfs(x,y+1)
            k=max(k,len(arr))
            print(x,y,arr,k)
            arr.pop()
            return 1
    return 0

dfs(0,0)
print(k)

# iehfklagcm
# pypy로 하면 15%에서 시간초과 나네 흠~ 이건 답을 봐야겠다