import sys
from collections import Counter
 
n = int(sys.stdin.readline())
n_arr = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
m_arr = list(map(int, sys.stdin.readline().split()))
 
cnt = Counter(n_arr)
 
for i in m_arr:
    print(cnt[i], end=' ')