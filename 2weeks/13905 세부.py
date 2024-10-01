import sys
from collections import deque
N, M = map(int, sys.stdin.readline().split())  # 집의 수, 다리의 수
S, E = map(int, sys.stdin.readline().split())  # 출발 위치, 도착 위치
'''
# 이진 탐색 + BFS 진행 -> 파라미터 리서치 ?
# 링크 : G3https://www.acmicpc.net/problem/13905 - 세부

# 빼빼로 -> 간선을 통해서 진행을 ㅎ나다.
1. 먼저 데이터 세팅 : 이중 리스트를 통해서 인덱스 통해서 해당 ( 번호, 가중치 ) 를 넣는다
2. visit 리스트 생성 ( N + 1 ) 로 생성 -> 큐를 생성한 뒤 큐 시작 지점을 넣음
3. 큐 시작한 후 visit 방문을 True로 변환 -> 큐를 leftpop함
4. weight >= mid (mid가 작을때만 BFS가 되도록 시행을 하는건가..? 작은걸,, 계속 찾는거 ?)

'''


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
    mid = (left + right) // 2  # 중간의 값을 가지는 것
    flag = False

    # BFS
    visit = [False] * (N+1)
    q = deque()
    q.append(S)  # 시작 부분을 넣는다.
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
