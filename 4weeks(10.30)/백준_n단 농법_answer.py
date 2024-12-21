'''
1. map 함수 사용하기 
2. while 문 사용해서 순환 반복하기 
3. 순환할시 break문 제대로 사용하기
https://www.acmicpc.net/problem/15723
'''

n = int(input())
logic = [-1] * 26
for i in range(n):          # a 는 b 이면서 c 일 수 없다 == 각 노드는 하나의 노드만 가리킨다
    x, y = map(lambda x: ord(x)-97, input().split(" is "))
    logic[x] = y
print("logic", logic)
m = int(input())
for i in range(m):          # m 이 최대 10개이고, n 은 26개이기 때문에 dfs 돌리듯 논법을 탐색
    visited = [False] * 26
    x, y = map(lambda x: ord(x)-97, input().split(" is "))
    while logic[x] != -1:   # 연결된 논법의 끝까지 탐색
        visited[x] = True  # 만약에 list[a] = True
        x = logic[x]  # list[a] = b
        if visited[x]:   # a ->b / b-> c / c->a 일 경우를 방지..
            break
        if x == y:            # 논법 성립하면 종료
            break

    print('T' if x == y else 'F')
