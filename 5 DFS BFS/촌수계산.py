n = int(input())+1
a,b = map(int,input().split())

G = [[] for _ in range(n)]

for _ in range(int(input())):
    i,j = map(int,input().split())
    G[i].append(j)
    G[j].append(i)

m = [0]*n

def bfs(G,v,m):
    Q = [v]
    m[v] = 1
    while Q:
        p = Q.pop(0)
        for i in G[p]:
            if not m[i]:
                Q.append(i)
                m[i] = m[p]+1

bfs(G,a,m)
print(m[b]-1)

# https://www.acmicpc.net/board/view/64738
# 반례