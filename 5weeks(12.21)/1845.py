def solution(nums):
    answer = 0
    nums = sorted(nums)
    answer = len(nums) / 2
    sorted_num = list(set(sorted(nums)))
    if len(sorted_num) < answer:
        answer = len(sorted_num)
    else:
        return answer
    return answer
