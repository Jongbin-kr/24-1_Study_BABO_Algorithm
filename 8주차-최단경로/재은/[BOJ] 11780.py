# 플로이드 2

n = int(input())
m = int(input())
INF = int(1e9)

cost = [[INF]* (n+1) for _ in range(n+1)]
path = [[[] for j in range(n+1)] for i in range(n+1) ]

for _ in range(m):
    a, b, t = map(int, input().split())
    if cost[a][b] > t:
        cost[a][b] = t
        path[a][b] = [a, b]
        

for i in range(1,n+1):
    for j in range(1, n+1):
        if i==j:cost[i][j] = 0

# cost 리스트 출력
        
for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            if a == b : 
                continue
            if cost[a][b] > cost[a][k] + cost[k][b]:
                cost[a][b] = cost[a][k] + cost[k][b]
                new_path = path[a][k] + path[k][b][1:]
                if len(new_path)>0:
                    path[a][b] = new_path
                    

for i in range(1, n+1):
    for j in range(1, n+1):
        if cost[i][j]==INF:
            cost[i][j] = 0

for a in cost[1:]:
    print(*a[1:])

for p in path[1:]:
    for b in p[1:]:
        print(len(b), *b)