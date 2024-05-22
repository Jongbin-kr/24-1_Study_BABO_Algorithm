X = int(input())

dp = [0] * (X+1)

# 보텀업 - 1부터 차례대로 작은 문제 구해나가기
for i in range(2,X+1):
    dp[i] = dp[i-1] + 1

    if i%2 == 0:
        dp[i] = min(dp[i], dp[i//2]+1)
    if i%3==0:
        dp[i] = min(dp[i], dp[i//3]+1)
    if i%5 == 0:
        dp[i] = min(dp[i], dp[i//5]+1)
    
print(dp[X])  