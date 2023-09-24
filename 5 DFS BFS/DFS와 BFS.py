# dfs bfs
n,m,v = map(int,input().split())
G = [[] for _ in range(n+1)]
for _ in range(m):
    a,b = map(int,input().split())
    G[a].append(b)
    G[b].append(a)

for i in G:
    i.sort()

dm = [0]*(n+1)
def dfs(G,v,dm):
    dm[v] = 1
    print(v,end=' ')
    for i in G[v]:
        if not dm[i]:
            dfs(G,i,dm)

from collections import deque
bm = [0]*(n+1)
def bfs(G,v,bm):
    queue = deque([v])
    bm[v] = 1

    while queue:
        p = queue.popleft()
        print(p,end=' ')
        for i in G[p]:
            if not bm[i]:
                bm[i] = 1
                queue.append(i)

dfs(G,v,dm)
print()
bfs(G,v,bm)