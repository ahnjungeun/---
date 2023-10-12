import heapq,sys
input=sys.stdin.readline
q = []

for _ in range(int(input())):
    n = int(input())
    if n:
        heapq.heappush(q,n)
    else:
        if len(q):
            print(heapq.heappop(q))
        else:
            print(0)