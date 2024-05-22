import sys
from collections import Counter

N=int(sys.stdin.readline())
cards=list(map(int,sys.stdin.readline().split()))
M=int(sys.stdin.readline())
find=list(map(int,sys.stdin.readline().split()))

cards_count=Counter(cards)

results=[cards_count[number] if number in cards_count.keys() else 0 for number in find]
for result in results:
    print(result)
