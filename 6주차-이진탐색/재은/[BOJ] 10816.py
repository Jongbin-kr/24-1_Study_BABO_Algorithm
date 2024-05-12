# 숫자 카드2
N = int(input())
cards = list(map(int, input().split()))
M = int(input())
entity = list(map(int, input().split()))

hash = {}

for c in cards:
    if c in hash:
        hash[c] += 1
    else:
        hash[c] = 1

for e in entity:
    if e in hash:
        print(hash[e], end=' ')
    else:
        print(0, end=' ')