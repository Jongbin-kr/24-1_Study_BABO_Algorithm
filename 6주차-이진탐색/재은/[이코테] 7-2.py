# 떡볶이 떡 만들기
N, M = map(int, input().split())
array = list(map(int, input().split()))

start = 0
end = max(array)
result = 0

while start<=end:
    mid = (start+end)//2
    length = 0
    for x in array:
        length += (x-mid if x>mid else 0)

    if length < M:
        end = mid-1
    else:
        result = mid
        start = mid+1

print(result)