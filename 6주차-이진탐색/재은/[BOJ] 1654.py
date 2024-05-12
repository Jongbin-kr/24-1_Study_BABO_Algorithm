import sys
K, N = map(int, input().split())
lines = []

for _ in range(K):
    lines.append(int(sys.stdin.readline()))

start = 1
end = max(lines)

while start<=end:
    mid = (start+end)//2
    sum = 0
    for _ in range(K):
        sum += lines[_]//mid
    if sum < N:
        end = mid-1
    elif sum >= N:
        start = mid+1

print(end)