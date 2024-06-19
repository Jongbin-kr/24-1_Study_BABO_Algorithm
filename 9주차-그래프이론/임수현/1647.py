import sys
input=sys.stdin.readline()
n,m =map(int,input.split())
memory=[]
# 그래프 표시 완
for _ in range(m):
    a,b,c=map(int,sys.stdin.readline().split())
    memory.append((a,b,c))
memory.sort(key=lambda x: x[2])

# union-find를 위한 테이블 작성
table = [i for i in range(n+1)]

def find_parent(table,x):
    if table[x]!=x:
        table[x]=find_parent(table,table[x])
    return table[x]

def union_parent(table,a,b):
    parent_a=find_parent(table,a)
    parent_b=find_parent(table,b)
    if parent_a>parent_b:
        table[parent_a]=parent_b
    else:
        table[parent_b]=parent_a

cost=0
high_cost=0
for a,b,c in memory:
    parent_a=find_parent(table,a)
    parent_b=find_parent(table,b)
    if parent_a!=parent_b:
        union_parent(table,a,b)
        if c>high_cost:
            high_cost=c
        cost+=c
answer=cost-high_cost
print(answer)
