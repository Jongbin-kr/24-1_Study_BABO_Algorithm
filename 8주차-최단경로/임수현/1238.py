import sys
import heapq
input = sys.stdin.readline
INF=int(1e9)

N,M,X=map(int,input().split())
graph=[[]for _ in range(N+1)]
# 입력에 맞춰 그래프 작성
for _ in range(M):
    start,end,dis=map(int,input().split())
    graph[start].append((end,dis))


def dijkstra(start):
    # disk생성, start정점에서 모든 정점까지의 거리를 저장
    disk=[INF]*(N+1)
    # memory 생성
    memory=[]
    # 메모리에 start정점을 거리 0으로 저장한다
    heapq.heappush(memory,(0,start))
    # start 정점의 거리를 0으로 disk에 저장한다
    disk[start]=0
    # memory가 비게되면 종료한다
    while memory:
        # 메모리의 정점들중 가장 가까운 정점을 꺼낸다
        distance,node = heapq.heappop(memory)
        # memory에서 가져온 정점의 거리가 disk에 적힌 거리보다 길면 최단 거리가 아니므로 버린다
        if distance>disk[node]:
            continue
        # 해당 노드에서 갈수있는 노드들을 메모리에 저장한다, 저장할때는 시작에서 현재 노드까지 거리 + 다음 노드의 거리로 저장한다
        for next_node,node_distance in graph[node]:    
            final_distance = distance+node_distance
            # 디스크에 저장한 해당 노드까지 거리가 새롭게 찾은 경로의 길이보다 길때만 탐색, 메모리 추가
            if disk[next_node]>final_distance:
                disk[next_node]=final_distance
                heapq.heappush(memory,(final_distance,next_node))
    return disk

result=[]
distance_to_home=dijkstra(X)
for i in range(1,N+1):
    table = dijkstra(i)
    total = table[X]+distance_to_home[i]
    result.append(total)
print(max(result))
