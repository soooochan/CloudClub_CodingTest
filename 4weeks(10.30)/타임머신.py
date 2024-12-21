# 문제
'''
문제

N개의 도시가 있다. 그리고 한 도시에서 출발하여 다른 도시에 도착하는 버스가 M개 있다. 각 버스는 A, B, C로 나타낼 수 있는데, A는 시작도시, B는 도착도시, C는 버스를 타고 이동하는데 걸리는 시간이다. 시간 C가 양수가 아닌 경우가 있다. C = 0인 경우는 순간 이동을 하는 경우, C < 0인 경우는 타임머신으로 시간을 되돌아가는 경우이다.
1번 도시에서 출발해서 나머지 도시로 가는 가장 빠른 시간을 구하는 프로그램을 작성하시오.
'''

'''
음수 간선에 관련하여 최단 경로 구하는 문제
1. 모든 간선이 양수인경우
2. 일부 간선이 음수인경우 
'''


import sys
input = sys.stdin.readline
INF = int(1e9)


def bellman_ford(start):
    dist[start] = 0

    # n번의 라운드를 반복
    for i in range(1, n + 1):
        # 매 라운드마다 모든 간선을 확인
        for j in range(m):
            now, next, cost = edges[j][0], edges[j][1], edges[j][2]
            # 현재 간선을 거쳐서 다른 노드로 이동하는 거리가 더 짧은 경우
            if dist[now] != INF and dist[next] > dist[now] + cost:
                dist[next] = dist[now] + cost
                # n번째 라운드에서도 값이 갱신된다면 음수 순환 존재
                if i == n:
                    return True

    return False


n, m = map(int, input().split())
edges = []
dist = [INF] * (n + 1)

for _ in range(m):
    a, b, c = map(int, input().split())
    edges.append((a, b, c))

negative_cycle = bellman_ford(1)

if negative_cycle:
    print(-1)
else:
    for i in range(2, n + 1):
        # 도달할 수 없는 경우
        if dist[i] == INF:
            print(-1)
        # 도달 가능한 경우
        else:
            print(dist[i])
