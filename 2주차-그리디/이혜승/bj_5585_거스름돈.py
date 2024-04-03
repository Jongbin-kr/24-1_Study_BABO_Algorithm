# 백준 5585 거스름돈

money =  int(input()) # '가격:' 넣었더니 백준 결과 틀림
coins = [500, 100, 50, 10, 5 ,1]

N = 1000 - money 
number = 0
for coin in coins:
    number = number + N//coin
    N = N%coin

print(number)