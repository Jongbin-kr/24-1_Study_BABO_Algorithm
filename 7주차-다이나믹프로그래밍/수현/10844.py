N=int(input())

result = [[0]*10 for _ in range(N)]
result[0] = [0,1,1,1,1,1,1,1,1,1]

for i in range(1,N):
    for k in range(10):
        if k==0:
            result[i][0]=result[i-1][1]
        elif k==9:
            result[i][9]=result[i-1][8]
        else:
            result[i][k]=result[i-1][k-1]+result[i-1][k+1]
print(sum(result[-1])%1000000000)
