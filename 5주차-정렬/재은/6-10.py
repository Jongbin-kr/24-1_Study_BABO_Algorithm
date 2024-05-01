# 위에서 아래로
# 계수정렬

N = int(input())
array = []
for _ in range(N):
    k = int(input())
    array.append(k)

array = sorted(array, reverse=True)

for i in array:
    print(i, end=' ')

def quicksort(array):
    if len(array) <=1 :
        return array
    pivot = array[0]
    tail = array[1:]

    left_side = [x for x in tail if x>=pivot]
    right_side = [x for x in tail if x<pivot]

    return quicksort(left_side) + [pivot] + quicksort(right_side)

for i in quicksort(array):
    print(i, end=' ')
