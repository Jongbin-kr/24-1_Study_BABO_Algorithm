N = int(input())

dp = [0] * (N+1)

def recursion(n):
    if dp[n] > 0 :
        # 이미 정의되어있음 => 푼 문제이다.
        return dp[n]
    
    if n==1:
        return 1

    if n == 2:
        return 3
    
    else:
        dp[n] = recursion(n-1) + recursion(n-2) * 2
        return dp[n]

print(recursion(N))