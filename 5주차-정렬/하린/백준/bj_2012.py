# 등수 매기기
import sys
n = int(sys.stdin.readline())

rank = []
for _ in range(n):
    rank.append(int(sys.stdin.readline()))

rank.sort()
ans = 0
for i in range(1, n+1):
    ans += abs(i-rank[i-1])

print(ans)