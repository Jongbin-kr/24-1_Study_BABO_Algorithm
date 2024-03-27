n = int(input())
w = list(map(int, input().split()))

l = len(w)-1

w.sort(reverse=True)

arr = []

for i in range(2*n):
    x = w[i] + w[l-i]
    arr.append(x)

print(min(arr))