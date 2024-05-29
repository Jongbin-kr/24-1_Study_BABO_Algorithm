# BABO 알고리즘 스터디 8주차
# 최단경로

#1 가장 빠른 길 찾기
import sys
input = sys.stdin.readline
INF = int(1e9) # 무한

n, m = map(int, input().split()) # 노드의 개수, 간선의 개수
start = int(input())

graph = [[] for i  in range(n+1)]
visited = [False] * (n+1)
distance = [INF] * (n+1)

for _ in range(m):
    a, b,  c  = map(int,  input().split())
    graph[a].append((b, c))  # a번 노드에서 b번 노드로 가는 비용이 C

def get_smallest_node(): 
    min_value = INF
    index = 0 # 가장 최단 거리가 짧은 노드
    for i  in range(1,  n + 1):
        if distance[i] < min_value and not visited[i]:
            min_value = distance[i]
            index = i
    return index

def dijkstra(start):
    distance[start] = 0 
    visited[start]  = True 
    for j in graph[start]:
        distance[j[0]] = j[1]
    for i  in range(n - 1):
        now = get_smallest_node() 
        visited[now] = True
        for j in graph[now]:
            cost = distance[now] + j[1]
            if cost < distance[j[0]]:
                distance[j[0]]  = cost

dijkstra(start)

for i  in  range(1, n + 1):
    if distance[i] == INF: # 도달할 수 없는 경우
        print("INFINITY")
    else: # 도달할 수 있는 경우
        print(distance[i])



#2 미래 도시
INF = int(1e9) 

n,  m = map(int,   input().split()) # 노드의 개수, 간선의 개수

graph = [[INF] * (n + 1) for _ in range(n+1)]

for a  in range(1, n + 1):
    for b in range(1,  n + 1):
        if a  == b:
            graph[a][b]  = 0

for _ in range(m):
    a, b = map(int,  input().split())
    graph[a][b] = 1 # A와 B가 서로에게 가는 비용은 1
    graph[b][a] = 1

x, k = map(int, input().split())  # 거쳐 갈 노드 X, 최종 목적지 노드 K

for k  in range(1, n + 1):
    for a in range(1,  n + 1): 
        for b in range(1,  n + 1):
            graph[a][b] = min(graph[a][b],   graph[a][k] + graph[k][b])

distance = graph[1][k] + graph[k][x]

if distance >= INF:  # 도달할 수 없는 경우
    print("-1")
else: # 도달할 수 있는 경우
    print(distance)


#3 전보
import heapq
import sys
input = sys.stdin.readline
INF = int(1e9) 

n,  m,   start = map(int,  input().split()) # 노드의 개수, 간선의 개수, 시작 노드

graph = [[] for i in range(n+1)]
distance = [INF] * (n + 1)
for _ in range(m):
    x, y, z  = map(int, input().split())
    graph[x].append((y, z)) # x번 노드에서 y번 노드로 가는 비용이 z

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start)) 
    distance[start]  = 0
    while q: 
        dist, now = heapq.heappop(q) # 가장 최단 거리가 짧은 노드에 대한 정보
        if distance[now] < dist:
            continue
        for i  in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dijkstra(start)

count = 0 # 도달할 수 있는 노드의 개수
max_distance = 0 # 도달할 수 있는 노드 중에서, 가장 멀리 있는 노드와의 최단 거리

for d in distance:
    if d  != INF:
        count += 1 # 도달할 수 있는 노드인 경우
        max_distance = max(max_distance, d)

print(count - 1, max_distance)