N, S = map(int, input().split())
arr = list(map(int, input().split()))

# 투 포인터 문제
start, end = 0, 0
sum_ = arr[0]
ans = 10001

while True:
    if sum_ < S:
        end += 1
        sum_ += arr[end]
        if end == N:
            break
    else:
        sum_ -= arr[start]

        ans = min(ans, end - start + 1)
        start += 1

if ans == 10001:
    print(0)
else:
    print(ans)
