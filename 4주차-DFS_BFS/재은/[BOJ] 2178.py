import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())

graph = []
for i in range(n):
    lst = list(map(int, input().rstrip()))
    graph.append(lst)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
cnt = 0


def bfs(a, b):
    queue = deque()
    queue.append((a, b))
    while queue:
        a, b = queue.popleft()
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            if graph[nx][ny] == 0:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[a][b] + 1
                queue.append((nx, ny))
    return graph[n - 1][m - 1]


print(bfs(0, 0))
