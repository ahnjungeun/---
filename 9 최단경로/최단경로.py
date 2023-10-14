import sys, heapq
input = sys.stdin.readline

n,m = map(int,input().split())
s = int(input())
G = [[] for _ in range(n+1)]
for _ in range(m):
    a,b,w = map(int,input().split())
    G[a].append((b,w))

inf = int(1e9)
d = [inf]*(n+1)
def dij(s):
    q = []
    # 시작노드 신경써라! 무지성 1 금지
    heapq.heappush(q,(0,s))
    d[s] = 0

    while q:
        dist,v = heapq.heappop(q)
        # 이 조건 잊지마라!
        if d[v]==dist:
            for i,w in G[v]:
                cost = dist+w
                if d[i] > cost:
                    d[i] = cost
                    heapq.heappush(q,(cost,i))

dij(s)
for i in d[1:]:
    print('INF' if i==inf else i)