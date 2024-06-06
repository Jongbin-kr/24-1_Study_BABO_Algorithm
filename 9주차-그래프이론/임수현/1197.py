import sys
input = sys.stdin.readline
V, E = map(int,input().split())
memory=[]
# cost순으로 정렬
for _ in range(E):
    a,b,c = map(int,input().split())
    memory.append((c,a,b))
memory.sort()

parent=[i for i in range(V+1)]

def find_parent(parent,x):
    if parent[x]!=x:
        parent[x]=find_parent(parent,parent[x])
    return parent[x]

def union_parent(parent,a,b):
    a=find_parent(parent,a)
    b=find_parent(parent,b)
    if a>b:
        parent[a]=b
    else:
        parent[b]=a

result=0
for cost,a,b in memory:
    if find_parent(parent,a)!=find_parent(parent,b):
        union_parent(parent,a,b)
        result+=cost
print(result)
