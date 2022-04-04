

# 일정이 주어지면 value를 계산해주는 함수

# N = int(input())
# i_d_ps = [[i, *map(int,input().split())] for i in range(1,N+1)]

# print(i_d_ps)
from itertools import combinations

def get_value(day_max, d_p):
    total_pay, today = 0, 1
    for [start_day, duration, pay]  in d_p:

        if start_day < today:
            # 지나쳐버린 경우 -> 다음일
            continue

        else:
            today = start_day
            # 시작 가능한 경우
            if today + duration -1 > day_max:
                # 시작하려면 하는데 제때 못 끝내면 그냥 다음일
                continue
            # 시작가능하고 끝맺음도 가능하면 수행
            today += duration
            total_pay += pay

    return total_pay

# get_value(7, [[7,2,200]])

N_main = int(input())
d_p_main = [[i+1, *list(map(int,input().split()))] for i in range(N_main)]

maximum = 0

for i in range(1, len(d_p_main)+1):
    for combi in combinations(d_p_main,i):
        value = get_value(N_main, combi)
        if maximum < value:
            maximum = value
print(maximum)
        