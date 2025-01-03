
n = int(input())
srr = [input() for _ in range(n)]
cnt = 0

# 입력받은 순서대로 저장해놓는다.
# G4https://www.acmicpc.net/problem/2179 - 비슷한 단어
index_arr = list(enumerate(srr))


''' 
    for 문으로 계속 돌면서 문자열의 길이를 찾는게 포인트,, 
'''


def check(x, y):
    cnt = 0
    min_len = min(len(x), len(y))
    for i in range(min_len):
        if x[i] == y[i]:
            cnt += 1
        else:
            return cnt
    return cnt


maxlen = [-1, -1, 0]
for x in range(n):
    for y in range(x+1, n):
        cur = check(srr[x][1], srr[y][1])
        if maxlen[2] < cur:
            maxlen[0] = x
            maxlen[1] = y
            maxlen[2] = cur


print(srr[maxlen[0]][1])
print(srr[maxlen[1]][1])
