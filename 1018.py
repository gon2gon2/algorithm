N, M = map(int, input().split())
tables = []
for i in range(N):
    tables.append(list(input()))

# 1. HEAD를 찾는다
# 2. 짝,짝 => == HEAD
# 3. 짝,홀 => != HEAD
# 4. 홀,짝 => != HEAD
# 5. 홀,홀 => == HEAD
W_paints = [[0 for i in range(M)] for j in range(N)]
B_paints = [[0 for i in range(M)] for j in range(N)]
HEAD = tables[0][0]

for i in range(N):
    for j in range(M):
        if (i+j)%2 == 0: # HEAD랑 같음
            W_paints[i][j] = tables[i][j] != 'B'
            B_paints[i][j] = tables[i][j] != 'W'
        else: # HEAD랑 다름
            W_paints[i][j] = tables[i][j] == 'B'
            B_paints[i][j] = tables[i][j] == 'W'


# 여기는 기준
points =[]
for i in range(N-7):
    for j in range(M-7):
        points.append((i,j))
# print(points)
# print(len(points))

answer = 99
for x,y in points:
    temp_1 = 0
    temp_2 = 0
    for i in range(x, x+8):
        temp_1 += sum(W_paints[i][y:y+8])
        temp_2 += sum(B_paints[i][y:y+8])
    
    lower = min(temp_1,temp_2)
    if lower < answer:
        answer = lower
print(answer)
'''
8 8
WBWBWBWB
BWBWBWBW
WBWBWBWB
BWBWBWBW
WBWBWBWB
BWBWBWBW
WBWBWBWB
BWBWBWBW

현재 0,0을 참조해서 비교중임
'''