from collections import deque
N, M, V = map(int, input().split())

graph = [[] for i in range(N+1)]
visited = [False] * (N+1)
for i in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(V):
    visited[V] = True
    print(V, end=' ')
    cur = sorted(graph[V])
    for i in cur:
        if not visited[i]:
            dfs(i)
    return

dfs(V)
print()
visited = [False] * (N+1)

def bfs(V):
    queue = deque()
    queue.append(V)
    while queue:
        V = queue.popleft()
        print(V, end=' ')
        visited[V] = True
        cur = sorted(graph[V])
        for i in cur:
            if not visited[i] and i not in queue:
                queue.append(i)

bfs(V)

