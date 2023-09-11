from collections import deque

# 큐를 사용해 pop한 노드의 인접노드를 큐에 넣고 방문처리 반복하기
def bfs(G,v,m):
    # 큐 생성하기
    queue = deque([v])
    # 시작노드는 while에서 처리할 수 없으므로 방문처리를 먼저 해주기
    m[v] = 1

    # 큐가 비었다는 건 방문을 다 끝냈다는 것
    while queue:
        # 맨앞 노드를 pop한 후
        p = queue.popleft()
        print(p)
        # 그 노드와 인접한 노드가
        for i in G[p]:
            # 미방문이면
            if not m[i]:
                # 큐에 넣고
                queue.append(i)
                # 방문처리하기
                m[i] = 1


G = [
    [], # 0번 노드가 없으면 비움
    [2,3,8], # 각 행 별로 꼭 정렬할 필요는 없으나,
    [1,7], # 관행적으로 작은 노드부터 순회하기에 정렬하는 게 좋대
    [1,4,5], # 물론! 이러면 순회순서가 변경되니 결과도 바뀜!
    [3,5], # 내림차순으로 정렬하고 순회하면 18327546으로 방문
    [3,4], # 오름차순으로 정렬하면 12387456
    [7],
    [2,6,8],
    [1,7]
]

# for i in G:
#     i.sort(reverse=True)
#     print(i)

m = [0]*9
bfs(G,1,m)