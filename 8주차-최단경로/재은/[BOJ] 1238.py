# 파티
import heapq

INF = int(1e9)
N, M, X = map(int, input().split())

def dijkstra(start):
    # 준비된 무한초기화 그래프 => distance 그래프로 소요시간 판단
    distance = [INF] * (N+1)
    distance[start] = 0
    q = []
    heapq.heappush(q, (0, start))
    while q:
        dist, cur = heapq.heappop(q)
        # 그래프에 저장된 값이 거리보다 큰 경우 => 초기화 필요
        if distance[cur]>=dist:
            for node, val in graph[cur]:
                # 시작점 start로부터 cur까지 - cur의 인접 노드들 계산
                # cur의 인접 노드들은 node이다.
                # 각 node별로 소요시간 계산 진행
                if dist + val < distance[node]:
                    # dist : start에서 cur까지의 소요시간
                    # val : cur에서 인접노드까지의 소요시간
                    distance[node] = dist+val
                    heapq.heappush(q, (dist+val, node))
    return distance

graph = [[] for _ in range(N+1)]
for _ in range(M):
    a, b, t = map(int, input().split())
    graph[a].append([b,t])

# X => 모든 노드로의 최단시간 구하기
# result : X에서 출발해 모든 노드로 도착할 때까지의 소요시간
result = dijkstra(X)
result[0] = 0

# 모든 노드 => X로의 최단시간 구하기
for i in range(1, N+1):
    if i!=X:
        # 시작점 X를 제외한 모든 노드에서 다익스트라 탐색
        res = dijkstra(i)
        # res : 시작점 i일 때의 distance 리스트
        # res[X] : 시작점 i, 도착점 X일 때 소요시간
        result[i] += res[X]

print(max(result))