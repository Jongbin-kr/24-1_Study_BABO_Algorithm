N, M = map(int, input().split())

dp = [10001] * (M+1)
dp[0] = 0
currency = []

for i in range(N):
    currency.append(int(input()))

# 보텀업 방식
    
for i in range(N):
    k = currency[i]
    for j in range(k, M+1):
        dp[j] = min(dp[j-k] + 1, dp[j])

if dp[M] == 10001:
    print(-1)
else:
    print(dp[M])