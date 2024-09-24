import sys


def find(x, n):
    global result
    if x < 500:  # 500 보다 작아지면
        return  # 끝
    if n == N:  # 운동 일 다 채우며
        result += 1  # 홧수 증가
        return
    x -= K
    for i in range(N):
        if not visited[i]:  # 사용하지 않았을 경우 탐색
            visited[i] = 1
            print("visited1 ", visited)
            find(x + kit[i], n+1)
            print("visited2 ", visited)
            visited[i] = 0


N, K = map(int, sys.stdin.readline().split())
kit = list(map(int, sys.stdin.readline().split()))
result = 0
visited = [0]*N
find(500, 0)
print(result)
