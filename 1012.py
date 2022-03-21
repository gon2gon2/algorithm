import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

T = int(input())
# T = 1

def bfs(x, y):
    '''
    1. x,y를 방문 처리해준다
    2. 상하좌우를 bfs함수에 넣어준다
    '''

    if x< 0 or y < 0 or x>=M or y>=N:
        return
    
    if graph[y][x] == 0:
        return

    graph[y][x] = 0
    
    bfs(x+1, y)
    bfs(x, y+1)
    bfs(x-1, y)
    bfs(x, y-1)



for t in range(T):
    
    # 가로 M, 세로 N, 배추 개수 K
    M, N, K = map(int, input().split())
    # M, N, K = 10, 8, 17

    cnt = 0

    # M과 N을 반대로 초기화하면 인덱싱을 편하게 할 수 있다.
    # graph = [[0]*N for _ in range(M)]
    graph = [[0]*M for _ in range(N)]

    for k in range(K):
        x,y = map(int,input().split())
        graph[y][x] = 1

    for i in range(N): # 세로
        for j in range(M): # 가로
            if graph[i][j] == 1:
                bfs(j,i)
                cnt += 1
    
    print(cnt)