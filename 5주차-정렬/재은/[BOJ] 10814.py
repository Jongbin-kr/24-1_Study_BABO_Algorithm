N = int(input())

members = []

for _ in range(N):
    member = input().split()
    members.append([int(member[0]), member[1]])

result = sorted(members, key=lambda member:member[0])

for k in result:
    print(k[0], k[1])