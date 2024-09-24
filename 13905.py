import sys
from collections import deque
N, M = map(int, sys.stdin.readline().split())
S, E = map(int, sys.stdin.readline().split())

# 노선 정보가 들어있는 리스트
edges = [[] for _ in range(N+1)]
answer = 0

for _ in range(M):
    h1, h2, k = map(int, sys.stdin.readline().split())
    edges[h1].append((h2, k))
    edges[h2].append((h1, k))


left = 1
right = 10 ** 6

# 이진 탐색
while left <= right:
    # 중간값을 계산하고 진행 ( 최대로 들고 갈 수 있는 빼빼로의 무게 )
    mid = (left + right) // 2 # 
    flag = False

    # BFS
    visit = [False] * (N+1)
    q = deque()
    q.append(S)
    visit[S] = True

    # 큐가 있는 동안 진행
    while q:
        now = q.popleft()
        if now == E:
            flag = True
            break

        # 큐가 있는 동안 진행
        for node, weight in edges[now]:
            if not visit[node] and weight >= mid:  # weight >= mid 4 
                q.append(node)
                visit[node] = True

    if flag:
        answer = mid
        left = mid + 1  # left -> 4
    else:
        right = mid - 1

print(answer)
