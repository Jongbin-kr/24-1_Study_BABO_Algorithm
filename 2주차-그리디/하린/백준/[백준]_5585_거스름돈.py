m = int(input())
n = 1000 - m
count = 0

money = [500, 100, 50, 10, 5, 1]

for coin in money:
    count += n // coin
    n %= coin

print(count)