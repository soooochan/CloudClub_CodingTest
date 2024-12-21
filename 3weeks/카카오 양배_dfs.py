def solution(n, info):
    global min_gap, final_answer
    min_gap = -1  # 최소 차이 초기화
    answer = [0] * 11
    final_answer = [-1]  # 승리할 수 없을 경우 반환할 기본값

    # 점수 계산 함수
    def compare(answer):
        a = 0  # 어피치 점수
        b = 0  # 라이언 점수
        for i in range(len(info)):
            if info[i] > 0 and info[i] >= answer[i]:
                a += 10 - i  # 어피치가 이긴 경우
            if answer[i] > 0 and answer[i] > info[i]:
                b += 10 - i  # 라이언이 이긴 경우
        return (b > a, b - a)

    # DFS 탐색 함수
    def dfs(L, cnt):
        global min_gap, final_answer

        # 종료 조건: 11번째 화살까지 계산하거나 남은 화살이 없을 때
        if L == 11 or cnt == 0:
            if cnt > 0:
                answer[10] += cnt  # 남은 화살을 0점에 모두 몰아 넣기

            # 점수 비교
            winner, gap = compare(answer)
            if winner:  # 라이언이 이긴 경우
                if gap > min_gap:  # 점수 차이가 클 때만 갱신
                    min_gap = gap
                    final_answer = answer.copy()  # 깊은 복사
                elif gap == min_gap:  # 점수 차이가 같을 때
                    # 낮은 점수를 더 많이 맞힌 경우를 선택
                    for i in range(10, -1, -1):  # 큰 점수부터 비교
                        if answer[i] > final_answer[i]:
                            final_answer = answer.copy()
                            break
                        elif answer[i] < final_answer[i]:
                            break

            return

        # info보다 더 많은 화살을 쏘는 경우
        if cnt > info[L]:
            answer[L] = info[L] + 1
            dfs(L + 1, cnt - answer[L])
            answer[L] = 0

        # 해당 점수 포기하는 경우
        dfs(L + 1, cnt)

    dfs(0, n)

    return final_answer
