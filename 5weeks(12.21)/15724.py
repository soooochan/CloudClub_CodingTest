import sys
input = sys.stdin.readline

n, m = map(int, input().split())
area = [list(map(int, input().split())) for _ in range(n)]

dp = [[0]*(m+1) for _ in range(n+1)]


# 열별로 합 누적시키기
for i in range(1, n):
    for j in range(m):
        dp[i][j] += dp[i-1][j]

# for 문 돌면서 input 값 넣기
for _ in range(int(input())):
    fromX, fromY, toX, toY = map(int, input().split())
    ans = sum(dp[toX-1][fromY-1:toY])
    if fromX > 1:
        ans -= sum(dp[fromX-2][fromY-1:toY])
    print(ans)
