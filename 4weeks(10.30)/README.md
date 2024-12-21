### 백준

## 백준 링크

- https://www.acmicpc.net/problem/15723

  - 1. map 함수 사용하기
  - 2. while 문 사용해서 순환 반복하기
  - 3. 순환할시 break문 제대로 사용하기

### 호식이 두마리 치킨

- https://www.acmicpc.net/problem/21278

### 타임머신 - 음수 간선에 관한 최단 경로 구하는 문제

- https://www.acmicpc.net/problem/11657

### BFS

from collections import deque

visited = [False] \* 5

def bfs(start):
queue = deque([start])
visited[start] = True

      while queue:
          x = queue.popleft()
          for x in graph[v]:
              if not visited[x]:
                  queue.append(x)
                  visited[x] = True

### DFS

visited = [False] \* 노드의 개수

def dfs(start):
visited[start] = True

for x in graph(start):
  if not visited[start]:
    dfs(start)

dfs(0)
