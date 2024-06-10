import sys
input = sys.stdin.readline
# 도시 분할 계획
def find_parent(parent, x):
    if parent[x]!=x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a > b :
        parent[a] = b
    else:
        parent[b] = a
    return parent


N, M = map(int, input().split())

parent = [i for i in range(N+1)]

# 경로를 비용 순으로 정렬한 후, 사이클 발생하게 하는 경로는 삭제
# 정렬을 위해서 튜플로 입력받기 => 튜플 첫번째 원소를 비용으로 설정
edges = []
result = 0
for _ in range(M):
    A, B, C = map(int, input().split())
    edges.append((C, A, B))

edges.sort()
max_path = 0

for edge in edges:
    if find_parent(parent, edge[1]) != find_parent(parent, edge[2]):
        # 사이클 발생 안함
        union(parent, edge[1], edge[2])
        result += edge[0]
        max_path = edge[0]

print(result - max_path)