n = int(input())
G = [[] for _ in range(n+1)]
for _ in range(n-1):
    a,b = map(int,input().split())
    G[a].append(b)
    G[b].append(a)

from collections import deque
def bfs(G,v,m):
    res = []
    queue = deque([v])
    m[v] = 1
    while queue:
        v = queue.popleft()
        for i in G[v]:
            if not m[i]:
                queue.append(i)
                m[i] = 1
                res.append((i,v))
    return sorted(res)

m = [0]*(n+1)
res = bfs(G,1,m)
for i,v in res:
    print(v)