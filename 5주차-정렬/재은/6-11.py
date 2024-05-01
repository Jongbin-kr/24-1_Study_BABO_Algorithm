# 성적이 낮은 순서로 학생 출력하기
# key 활용하여 sort

N = int(input())
students = []

for _ in range(N):
    student = input().split()
    students.append([student[0], int(student[1])])

def setting(ary):
    return ary[1]

result = sorted(students, key=setting)

for i in range(N):
    print(result[i][0])
