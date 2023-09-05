n = int(input())+1
e = int(input())

G = [[] for _ in range(n)]
m = [0]*n

for _ in range(e):
    a,b = map(int,input().split())
    G[a].append(b)
    # 무방향 그래프니까 양쪽 연결해주기
    G[b].append(a)

def dfs(G,v,m):
    m[v] = 1
    for i in G[v]:
        if not m[i]:
            dfs(G,i,m)

dfs(G,1,m)
print(sum(m)-1)