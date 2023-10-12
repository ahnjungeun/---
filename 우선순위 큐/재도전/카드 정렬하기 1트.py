import sys, heapq
input = sys.stdin.readline

n=int(input())
l = []
for _ in range(n):
    heapq.heappush(l,int(input()))

s=0
for _ in range(n-1):
    x = heapq.heappop(l)
    y = heapq.heappop(l)
    s += x+y
    heapq.heappush(l,x+y)

print(s)

# 어려운 건 아닌데 생각하는데 오래 걸려서 다음에 다시 풀어보기로!