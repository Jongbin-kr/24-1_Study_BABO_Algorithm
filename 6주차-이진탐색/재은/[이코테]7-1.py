# 부품 찾기
N = int(input())
storage = sorted(list(map(int,input().split())))
M = int(input())
customer = list(map(int,input().split()))

def binary_search(storage, start, end, x):
    while start<=end:
        mid = (start+end)//2
        if storage[mid] == x:
            return mid
        elif storage[mid] > x:
            end = mid - 1
        else:       # 인덱스 정비
            start = mid + 1
    return False

for c in customer:
    result = binary_search(storage, 0, N-1, c)
    if not result:
        print('no', end=' ')
    else:
        print('yes', end=' ')
