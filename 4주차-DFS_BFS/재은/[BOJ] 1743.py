#2중 포문 -> cnt = 1로 시작 (1인 노드만 탐색)
#동서남북으로 dfs 
#dfs로 동서남북 볼 때 visited 여부 확인
#1일 경우 cnt += 1 하며 reutrn, 0일 경우 그냥 return
#동서남북이 전부 0일 경우, cnt값 return

import sys

sys.setrecursionlimit(10000)

N, M, K = map(int, input().split())

graph = [[0] * M for _ in range(N)]

for i in range(K):
    x, y = map(int, input().split())
    graph[x-1][y-1] = 1

dx = [-1,1,0,0]
dy = [0,0,-1,1]
visited = [[0] * M for _ in range(N)]

def dfs(x,y):
    global cnt
    for _ in range(4):
        nx = x + dx[_]
        ny = y + dy[_]
        if -1>=nx or -1>=ny or nx>=N or ny>=M:
            continue
        #visited는 0인 상태, 음식물 여부 확인
        if graph[nx][ny] == 1 and visited[nx][ny] == 0:
            visited[nx][ny] = 1
            cnt += 1
            dfs(nx,ny)

tmp_list = []

for i in range(N):
    for j in range(M):
        if graph[i][j] == 1 and visited[i][j] == 0:
            cnt = 0
            dfs(i,j)
            tmp_list.append(cnt)

print(max(tmp_list))
