'''

맨 처음부터 차근차근 더하면 되는 거 아닌가?
sort로 정렬 ( reverse=True)

투 포인터 문제로 가는 것
1. while문을 통해서 
2. arr[start], arr[end] ( end로 늘리다가 , 만약 값이 초과되면 arr[start]를 더하고 더한 값을 빼기 Start + 1 )
3. 길이 : end - start
4. min 값으로 최소화 

'''

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
