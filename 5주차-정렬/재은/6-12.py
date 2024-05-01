# 두 배열의 원소 교체
# 두 배열을 정렬한 후, A 배열의 맨 앞 세 개와 B 배열의 맨 뒤 세 개를 교체.

N, K = map(int, input().split())

A = sorted(list(map(int, input().split())))
B = sorted(list(map(int, input().split())),reverse=True)

for _ in range(K):
    if A[_]<B[_]:
        A[_] = B[_]
    else:continue

# A의 맨 뒤 (N-K)개, B의 맨 뒤 K개 출력.
print(sum(A))