import heapq
import sys

N, M, C = map(int, input().split())
INF = int(1e9)

# 정보를 담는다 => 전달되는 시간
graph = [[] for _ in range(N+1)]

distance = [INF] * (N+1)

for _ in range(M):
    X, Y, Z = map(int, input().split())
    graph[X].append((Y, Z))

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start]=0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now]<distance:
            continue
        for i in graph[now]:
            cost = dist + i[1]
        if cost < distance[i[0]]:
            distance[i[0]] = cost
            heapq.heappush(q,(cost,i[0]))

dijkstra(C)

# 도달 가능한 노드 개수
count = 0
max_distance = 0

for d in distance:
    if d < INF:
        count += 1
        max_distance = max(d, max_distance)

print(count-1, max_distance)