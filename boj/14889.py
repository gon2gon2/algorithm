from itertools import combinations


N = int(input())
status = [list(map(int, input().split())) for _ in range(N)]

all_memebers = set(range(N))


answer = 10000
def get_overall(team,status):
    overall = 0
    # cnt = 0
    # while cnt != len(team):
    #     x = team.pop(0)
    #     for i in team:
    #         overall += status[x][i]
    #     team.append(x)
    #     cnt +=1

    for i in range(len(team)):
        other_people = team[:i] + team[i+1:]
        for j in other_people:
            overall += status[team[i]][j]

    return overall


for A_team in combinations(all_memebers,N//2):
    B_team = all_memebers.difference(A_team)
    
    answer = min(answer,abs(get_overall(list(A_team),status) - get_overall(list(B_team),status)))

print(answer)
    