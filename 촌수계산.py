n = int(input())+1
a,b = map(int,input().split())

G = [[] for _ in range(n)]

for _ in range(int(input())):
    i,j = map(int,input().split())
    G[i].append(j)
    G[j].append(i)

m = [0]*n

def bfs(G,v,m):
    global b
    Q = [v]
    m[v] = 1
    c=0
    while Q:
        # c+=1
        p = Q.pop(0)
        print('p,c',p,c)
        for i in G[p]:
            
            if not m[i]:
                Q.append(i)
                m[i] = 1

            if i == b:
                return(c)
        c+=1

r = bfs(G,a,m)
print(r if r else -1)

# https://www.acmicpc.net/board/view/64738
# 반례