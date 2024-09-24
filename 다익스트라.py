import sys
import heapq
INF = sys.maxsize
N, M = map(int, sys.stdin.readline().split())
s, e = map(int, sys.stdin.readline().split())
# edges 저장
edges = [[] for _ in range(N+1)]
answer = 0
distance = [0] * (N+1)

for _ in range(M):
    h1, h2, k = map(int, sys.stdin.readline().split())
    edges[h1].append((h2, k))
    edges[h2].append((h1, k))

h = []
heapq.heappush(h, (-INF, s))
distance[s] = -INF

while h:
    dist, now = heapq.heappop(h)
    dist = -dist
    print("dist2", dist, now)

    # edges 저장
    if distance[now] > dist:  # edges 저장
        continue

    for node, d in edges[now]:
        print("dist", node, d)
        cost = min(dist, d)
        if cost > distance[node]:
            distance[node] = cost
            heapq.heappush(h, (-cost, node))

print(distance[e])
