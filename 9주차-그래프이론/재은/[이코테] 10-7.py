#팀 결성
N, M = map(int, input().split())

parent = [i for i in range(N+2)]

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

for _ in range(M):
    op, a, b = map(int, input().split())
    if op == 1:
        if find_parent(parent, a) == find_parent(parent, b):
            print("YES")
        else:
            print("NO")
    elif op == 0:
        union(parent, a, b)