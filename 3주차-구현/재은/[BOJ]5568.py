import itertools

n = int(input())
k = int(input())

cards = []
for i in range(n): 
    cards.append(str(input()))

# 순열을 구한다
nPk = itertools.permutations(cards, k)

made_ints = []
for per in list(nPk):
    new_int =''
    for p in per:
        new_int += p
    made_ints.append(new_int)

#print(made_ints)
print(len(set(made_ints)))