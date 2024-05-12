# 숫자 카드 2
N = int(input())
cards = list(map(int, input().split()))
M = int(input())
entity = list(map(int, input().split()))

results = [0] * M
cards.sort()

def binarysearch(start, end, x):
    global cards
    while start<=end:
        mid = (start+end)//2
        if cards[mid] > x :
            end = mid - 1
        elif cards[mid] < x:
            start = mid + 1
        elif cards[mid] == x:
            return cards.count(x)
    return None

for e in entity:
    result = binarysearch(0, N-1, e)
    if result is not None:
        print(result, end=' ')
    if result is None:
        print(0, end=' ')

