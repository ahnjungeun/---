import heapq,sys
# 이진탐색문제 빠르게 입력받기!!
input=sys.stdin.readline
q = []
for _ in range(int(input())):
    n = int(input())
    if n:
        heapq.heappush(q,-n)
    else:
        if q:
            print(-heapq.heappop(q))
        else:
            print(0)