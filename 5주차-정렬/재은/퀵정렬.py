# 퀵 정렬 - 기준을 설정한 다음, 큰 수와 작은 수 교환
# 피봇을 기준으로 리스트를 반으로 나눈다.

array = [5,7,9,0,3,1,6,2,4,8]

def quicksort(array, start, end):
    if start>=end:
        return
    pivot = start
    left = start + 1
    right = end
    while left <= right:
        while left <= end and array[left] <= array[pivot]:
            left += 1
        while right>start and array[right]>=array[pivot]:
            right -= 1
        if left > right:
            array[right], array[pivot] = array[pivot], array[right]
        else:
            array[left], array[right] = array[right], array[left]
    quicksort(array, start, right-1)
    quicksort(array, right+1, end)

quicksort(array, 0, len(array)-1)

print(array)