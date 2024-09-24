import sys
import copy

n = list(sys.stdin.readline().rstrip())
# 0과 1의 개수를 세기
count_0 = n.count('0')
count_1 = n.count('1')

new_number = ['0'] * (count_0 // 2) + ['1'] * (count_1 // 2)

print("".join(new_number))
