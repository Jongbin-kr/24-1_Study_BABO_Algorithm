import sys
import heapq
INF = 1e10
def input(): return sys.stdin.readline().rstrip()

def dijkstra(s):
    global x
    dist = [INF] * (n+1)
    q = []
    heapq.heappush(q,(s,0))
    while q:
        w,d = heapq.heappop(q)
        if dist[w] < d:
            continue
        for nxt,c in graph[w]:
            if dist[nxt] > d + c:
                dist[nxt] = d+c
                heapq.heappush(q,(nxt,d+c))
    if s != x:
        return dist[x]
    return dist

n,m,x = map(int,input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a,b,c = map(int,input().split())
    graph[a].append((b,c))
node2x = [0] * (n+1)
for i in range(1,n+1):
    if i != x:
        node2x[i] = dijkstra(i)
x2node = dijkstra(x)

print(max([x2node[i] + node2x[i] for i in range(1,n+1) if i != x]))