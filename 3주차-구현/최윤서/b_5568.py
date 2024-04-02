# 카드 놓기

n = int(input())
k = int(input())

cards = [int(input()) for _ in range(n)]

visited = [0] * n
stack = []
numbers = set()

def dfs(depth):
    if depth == k:
        numbers.add(''.join(map(str, stack)))
        return 
    for i in range(n):
        if visited[i]:
            continue
        stack.append(cards[i])
        visited[i] = 1
        dfs(depth+1)
        stack.pop()
        visited[i] = 0 

dfs(0)

print(len(numbers))
