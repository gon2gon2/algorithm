'''
0: 빈칸
1: 벽
2: 바이러스

0의 좌표를 전부 기록한 다음, n개만 1로 바꾼다.
0에 벽을 세운다
1을 만나기 전까지 바이러스를 퍼트린다(i,j 상하좌우)
0의 개수를 return

나의 패인: bfs를 너무 깊게 생각함. 단순하게 할것

blank_space를 일일이 다 구하느라 순회가 많다
차라리 재귀를 사용ㄱ하거나 2중포문을 한번만 돌게 만들자
for i in range(x,n*m):
    c = i//m
    d = i % m

'''

dx, dy = [-1,1,0,0], [0,0,-1,1]
def spread_virus(x,y, graph):
    graph[x][y] = 2

    for i in range(4):
        nx, ny = x+dx[i], y+dy[i]
        if 0<=nx<N  and 0 <= ny < M:
            if graph[nx][ny] == 0:
                spread_virus(nx,ny, graph)
    


N, M = map(int, input().split())
# input 받을 때 순회시켜서 blank append하는 최적화 가능
lab = [list(map(int, input().split())) for _ in range(N)]
blank_space = []

for i in range(N):
    for j in range(M):
        if lab[i][j] == 0:
            blank_space.append((i,j))



maximum = 0
from itertools import combinations
for points in combinations(blank_space,3):
    temp = [row[:] for row in lab]

    for (x,y) in points:
        temp[x][y] = 1

    for i in range(N):
        for j in range(M):
            if temp[i][j] == 2:
                spread_virus(i,j,temp)
    
    safe_space = 0
    maximum = max(maximum, sum(_.count(0) for _ in temp))
    if maximum < safe_space:
        maximum = safe_space
print(maximum)
