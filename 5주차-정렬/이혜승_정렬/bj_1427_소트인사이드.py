N = int(input())

li = []
for i in str(N):
    li.append(int(i))

# li = list(map(int, str(N)))

li.sort(reverse=True) # 내림차순

for i in li :
    print(i, end='')
    