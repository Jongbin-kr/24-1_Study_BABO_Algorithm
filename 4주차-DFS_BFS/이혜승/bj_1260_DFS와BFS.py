# 그래프를 DFS로 탐색한 결과와 BFS로 탐색한 결과를 출력하는 프로그램을 작성하시오. 
# 단, 방문할 수 있는 정점이 여러 개인 경우에는 정점 번호가 작은 것을 먼저 방문하고, 더 이상 방문할 수 있는 점이 없는 경우 종료한다. 
# 정점 번호는 1번부터 N번까지이다.

N, M, V = map(int, input().split())



# 행렬 만들기
graph = [[0]*(N+1) for _ in range(N+1)]

for _ in range(0,M):
    a, b = map(int, input().split())
    graph[a][b] = graph[b][a] = 1

# 방문 리스트 행렬
visited1 = [0]*(N+1)
visited2 = visited1.copy()

# dfs 함수 만들기
def dfs(V):
    visited1[V] = 1 # 방문처리
    print(V, end = ' ')
    for i in range(1, N+1):
        if graph[V][i] == 1 and visited1[i] == 0:
            dfs(i)

# bfs 함수 만들기
def bfs(V):
    queue = [V]
    visited2[V] = 1 # 방문처리
    while queue:
        V = queue.pop(0) # 방문 노드 제거
        print(V, end = ' ')
        for i in range(1, N+1):
            if(visited2[i] == 0 and graph[V][i] == 1):
                queue.append(i)
                visited2[i] = 1 # 방문처리

dfs(V)
print()
bfs(V)