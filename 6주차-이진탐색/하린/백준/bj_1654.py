
import sys
input = sys.stdin.readline

k, n = map(int, input().split())
lan = [int(input()) for _ in range(k)]

def binary_search(length_list):
    H = max(length_list)
    L = 1

    while L <= H:
        M = (H + L) // 2
        cnt = sum([x//M for x in lan])
        if cnt < n:
            H = M - 1
        else:
            L = M + 1
    return H

print(binary_search(lan))