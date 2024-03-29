# 카드 놓기
# n장의 카드 중에서 k개를 선택해서 만들 수 있는 정수의 개수 구하기


from itertools import permutations
n = int(input()) #카드 개수
k= int(input()) # 뽑는 카드 수

numbers = [input() for _ in range(n)]

new_nums = set()
for c in permutations(numbers, k):
    new_nums.add("".join(c))

print(len(new_nums))


# permutations(nums, k): 순열
# combinations(arr, 2) : 조합