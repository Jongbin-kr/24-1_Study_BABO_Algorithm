N = int(input())

skills = list(map(int, input().split()))

sorted_skills = sorted(skills)

team_skills_list=[]

for i in range(0,N):
    team_skills = sorted_skills[i] + sorted_skills[-1-i]
    team_skills_list.append(team_skills)

min = min(team_skills_list)
print(min)

