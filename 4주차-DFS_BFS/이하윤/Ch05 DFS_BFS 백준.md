# 1260번 DFS와 BFS

```python
from collections import deque

n, m, v = map(int, input().split())
graph = [[] for _ in range(n+1)]

def dfs(graph, v):
    visited = [False] * (len(graph))
    stack = [v]
    result = []

    while stack:
        node = stack.pop()
        if not visited[node]:
            visited[node] = True
            result.append(node)
            stack.extend(sorted(graph[node], reverse=True))
    
    return result

def bfs(graph, v):
    visited = [False] * (len(graph))
    queue = deque([v])
    result = []

    while queue:
        node = queue.popleft()
        if not visited[node]:
            visited[node] = True
            result.append(node)
            queue.extend(sorted(graph[node]))
    
    return result
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(n+1):
    graph[i].sort()

print(" ".join(map(str, dfs(graph, v))))
print(" ".join(map(str, bfs(graph, v))))
```
# 2178번 미로탐색
```python
from collections import deque

N, M = map(int, input().split())
maze = [input() for _ in range(N)]

def min_steps_to_exit(maze):
    n = len(maze)
    m = len(maze[0])

    dx = [-1, 1, 0, 0]  # 상하좌우 이동
    dy = [0, 0, -1, 1]

    queue = deque([(0, 0, 1)])  # 시작 위치와 이동한 칸 수를 큐에 저장
    visited = set()  # 방문한 위치를 저장할 집합

    while queue:
        x, y, steps = queue.popleft()
        if (x, y) == (n-1, m-1):  # 목표 지점에 도달했을 때
            return steps
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and maze[nx][ny] == '1' and (nx, ny) not in visited:
                visited.add((nx, ny))
                queue.append((nx, ny, steps + 1))

# 결과 출력
print(min_steps_to_exit(maze))
```
# 1743번 음식물 피하기
```python
from collections import deque

N, M, K = map(int, input().split())
trash = [tuple(map(int, input().split())) for _ in range(K)]

def find_largest_trash(N, M, K, trash):
    # 음식물이 있는 위치를 2차원 리스트로 표현
    grid = [[0] * M for _ in range(N)]
    for r, c in trash:
        grid[r-1][c-1] = 1

    # BFS를 이용하여 음식물의 크기를 구함
    def bfs(r, c):
        count = 0
        queue = deque([(r, c)])
        while queue:
            x, y = queue.popleft()
            if grid[x][y] == 1:
                count += 1
                grid[x][y] = 0  # 음식물을 방문한 것으로 처리
                for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < N and 0 <= ny < M and grid[nx][ny] == 1:
                        queue.append((nx, ny))
        return count

    max_trash_size = 0
    for i in range(N):
        for j in range(M):
            if grid[i][j] == 1:
                max_trash_size = max(max_trash_size, bfs(i, j))

    return max_trash_size

# 결과 출력
print(find_largest_trash(N, M, K, trash))
```
