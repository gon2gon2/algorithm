'''
개선 방향
1. W_paints, B_paints따로 두지 말고, B랑 W의 빈도 수를 계산해 둘 중 하나의 case만 생각하도록 수정

'''
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

for i in range(N):
    for j in range(M):
        if (i+j)%2 == 0: 
            W_paints[i][j] = tables[i][j] != 'B'
            B_paints[i][j] = tables[i][j] != 'W'
        else: 
            W_paints[i][j] = tables[i][j] == 'B'
            B_paints[i][j] = tables[i][j] == 'W'


# 여기는 기준점
points =[]
for i in range(N-7):
    for j in range(M-7):
        points.append((i,j))

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