# https://www.acmicpc.net/problem/3190

'''
1. 먼저 그래프를 0으로 채워준다. 
2. 사과 위치는 모두 2로 채워준다.
3. 앞으로 뱀이 차지하고 있는 부분은 1로 채워줄 것이다.
4. 방향 전환을 맞춰 L 또는 D를 한다. 
'''

from collections import deque

n = int(input())
m = int(input())

graph = [[0] * n for _ in range(n)]


for i in range(m):
    x, y = map(int, input().split(" "))
    graph[x-1][y-1] = 2


l = int(input())
dirDict = dict()
queue = deque()
queue.append((0, 0))


def turn(alpha):
    global direction
    if alpha == 'L':
        direction = (direction - 1) % 4
    else:
        direction = (direction + 1) % 4


for i in range(l):
    x, c = input().split()
    dirDict[int(x)] = c

x, y = 0, 0
graph[x][y] = 1
cnt = 0
direction = 0
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
while True:
    cnt += 1
    x += dx[direction]
    y += dy[direction]
    if x < 0 or x >= n or y < 0 or y >= n:
        break

    if graph[x][y] == 2:
        graph[x][y] = 1
        queue.append((x, y))
        if cnt in dirDict:
            turn(dirDict[cnt])

    elif graph[x][y] == 0:
        graph[x][y] = 1
        queue.append((x, y))
        tx, ty = queue.popleft()
        graph[tx][ty] = 0
        if cnt in dirDict:
            turn(dirDict[cnt])

    else:
        break
