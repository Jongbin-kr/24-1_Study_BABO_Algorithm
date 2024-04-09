# DFS와 BFS

"""
n: 정점의 개수
m: 간선의 개수
v: 탐색을 시작할 정점의 번호
"""
from collections import deque

n, m, v = map(int, input().split())

# 초기 그래프 셋팅
graph = [[]*(n+1) for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    graph[a].sort()
    graph[b].sort()

visited_1 = [False]*(n+1)   # DFS 방문기록
visited_2 = [False]*(n+1)   # BFS 방문기록

# DFS
def dfs(v):
    visited_1[v] = True     # 탐색을 시작할 node 방문처리
    print(v, end=" ")
    for i in graph[v]:
      if not visited_1[i]:
        dfs(i)

# BFS
def bfs(v):
    q = deque([v])
    visited_2[v] = True
    while q:
        v = q.popleft()
        print(v, end=" ")
        for i in graph[v]:
          if not visited_2[i]:
            q.append(i)
            visited_2[i]=True


dfs(v)
print()
bfs(v)