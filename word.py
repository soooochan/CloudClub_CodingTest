import sys
import copy

n = int(sys.stdin.readline().rstrip())
set1 = list(sys.stdin.readline().rstrip())


answer = 0
for i in range(n-1):
    set2 = list(sys.stdin.readline().rstrip())
    # 중복 제거
    if abs(len(set1) - len(set2)) > 1 or len(set(set1).difference(set(set2))) > 1:
        continue

    for target in set1:
        if target in set2:
            set2.remove(target)

    # print("set2", set2)
    if len(set2) <= 1:
        answer += 1


print("answer", answer)
