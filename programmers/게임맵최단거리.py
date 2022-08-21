"""
최단경로니까 BFS로 하면 좋을 것 같은데?
pop한다(현재 몇번쨰 move인지도 같이 기록)
1. 목적지? -> return
2. else: 방문한 적이 없으면서 갈 수 있는 곳을 append한다.
"""
from collections import deque

dx = [0,0,-1,1]
dy = [1,-1,0,0]
# n 가로 m 세로
def solution(maps):
    n = len(maps[0]) # x
    m = len(maps)    # y
    target = (n-1, m-1)
    
    queue = deque([[(0,0), 1]])
    visited = [[False]*n for _ in range(m)]
    
    while queue:
        now_pos, now_step = queue.popleft()
        visited[now_pos[1]][now_pos[0]] = True
        
        if (now_pos[0], now_pos[1]) == target:
            return now_step
        
        for i in range(4):
            nx = now_pos[0] + dx[i]
            ny = now_pos[1] + dy[i]
            
            if 0<= nx < n and 0 <= ny < m and not visited[ny][nx] and maps[ny][nx]:
                queue.append([(nx, ny), now_step+1])
                visited[ny][nx] = True
                
    return -1