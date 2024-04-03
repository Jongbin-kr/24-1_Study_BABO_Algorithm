# 특정 거리의 도시 찾기
# BFS
import sys
from collections import deque

N, M, K, X = map(int, input().split())
graph = [[] for _ in range(N+1)]

for i in range(M):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)

result = [-1] * (N+1)
result[X] = 0

def bfs(graph, start, result):
    queue = deque([start])
    while queue:
        v = queue.popleft()
        if result[v]>K:
            break
        for i in graph[v]:
            if result[i] == -1:
                queue.append(i)
                result[i] = result[v] + 1
 
    return result

result = bfs(graph, X, result)
flag = False

for i in range(len(result)):
    if result[i] == K:
        flag = True
        print(i)

if not flag:
    print(-1)
       