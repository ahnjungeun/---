# 입력 받기
import sys
input = sys.stdin.readline

# n 노드 수, m 입력 수
n,m = map(int,input().split())
# v 시작노드
v = int(input())

G = [[] for _ in range(n+1)]
for _ in range(m):
    # a b 인접노드 c 가중치
    a,b,c = map(int,input().split())
    G[a].append((b,c))

# 방문여부, 최단거리 기록 리스트
m = [0]*(n+1)
INF = int(1e9)
d = [INF]*(n+1)

# 미방문 노드 중 최단거리 노드 인덱스 찾기
def find_min_d():
    # 최단거리 초기화
    min_d = INF
    # 최단거리인 노드 인덱스
    idx = 0
    for i in range(1,n+1):
        if not m[i] and d[i]<min_d:
            min_d = d[i]
            idx = i
    return idx

def dij(start):
    d[start] = 0
    m[start] = 1

    for v,w in G[start]:
        d[v] = w

    for _ in range(n-1):
        now = find_min_d()
        m[now] = 1
        for v,w in G[now]:
            cost = d[now] + w
            d[v] = min(d[v],cost)

dij(v)
print(*d)