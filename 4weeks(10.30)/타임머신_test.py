import sys
input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split())
edges = []
dist = [INF] * (n+1)  # n = 도시의 개수

# 난 아직도 n : 도시의 개수 m : 버스 노선의 개수


def bellman_ford(start):
    dist[start] = 0
    # n 번의 라운드를 반복
    for i in range(1, n+1):  # n : 도시의 개수
        # 매 라운드마다 모든 간선을 확인
        for j in range(m):  # m : 버스 노선의 개수
            now, next, cost = edges[j][0], edges[j][1], edges[j][2]
            # 현재 간선을 거쳐서 다른 노드로 이동하는 거리가 더 짧은 이유
            if dist[now] != INF and dist[next] > dist[now] + cost:
                dist[next] = dist[now] + cost
                # n번째 라우드에서부터 값이 갱신된다면
                if i == n:
                    return True
    return False


for _ in range(m):
    a, b, c = map(int, input().split())
    edges.append((a, b, c))

negative_cycle = bellman_ford(1)

if negative_cycle:
    print(-1)
else:
    for i in range(2, n + 1):
        # 도달할 수 없는 경우 -> 무한 루프
        if dist[i] == INF:
            print(-1)
        # 도달 가능한 경우
        else:
            print("dist", dist)
            print(dist[i])
