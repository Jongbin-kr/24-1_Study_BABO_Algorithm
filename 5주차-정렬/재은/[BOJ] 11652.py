N = int(input())
numbers = []
count = {}
for _ in range(N):
    k = int(input())
    numbers.append(k)
    count[k] = 0

for n in numbers:
    count[n] += 1

max_value = max(count.values())
new_count = []

for c in count.items():
    if c[1]==max_value:
        new_count.append(c[0])

print(min(new_count))