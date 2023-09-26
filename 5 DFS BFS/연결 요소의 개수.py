import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(G,v,m):
    m[v] = 1
    for i in G[v]:
        if not m[i]:
            dfs(G,i,m)

from collections import deque

def bfs(G,v,m):
    queue = deque([v])
    m[v] = 1
    while queue:
        v = queue.popleft()
        for i in G[v]:
            if not m[i]:
                queue.append(i)
                m[i] = 1


n,m = map(int,input().split())
G = [[] for _ in range(n+1)]
for _ in range(m):
    a,b = map(int,input().split())
    G[a].append(b)
    G[b].append(a)

c=0
m = [0]*(n+1)
for i in range(1,n+1):
    if not m[i]:
        bfs(G,i,m)
        # dfs(G,i,m)
        c+=1
print(c)