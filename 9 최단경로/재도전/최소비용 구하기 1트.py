import sys,heapq
input = sys.stdin.readline

n = int(input())+1
m = int(input())
G = [[] for _ in range(n)]
for _ in range(m):
    a,b,w = map(int,input().split())
    G[a].append((b,w))

src, dest = map(int,input().split())
inf = int(1e9)
d = [inf]*n

def dij(src):
    queue = []
    heapq.heappush(queue,(0,src))
    d[src] = 0

    while queue:
        dist,v = heapq.heappop(queue)
        if dist == d[v]:
            for i,w in G[v]:
                # 여기 수정해서 시간초과 해결함
                cost = dist+w
                if d[i] > cost: # 원래 >= 였음
                    d[i] = cost
                    heapq.heappush(queue,(d[i],i))

dij(src)
print(d[dest])


# 벨로그에 써놨다! 모르겠으면 확인하기~

# 시간초과 : https://resilient-923.tistory.com/139
# 메모리초과 : https://velog.io/@kms9887/BOJ-1916-%EC%B5%9C%EC%86%8C%EB%B9%84%EC%9A%A9-%EA%B5%AC%ED%95%98%EA%B8%B0