visited = [False] 

def dfs(start):
    visited[start] = True

    for x in graph(start):
        if not visited[start]:
            dfs(start)

dfs(0)