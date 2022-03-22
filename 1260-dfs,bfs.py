# N : 정점 개수
# M : 간선 개수
# V : 시작할 정점
N, M, V = map(int, input().split())
graph = [[]for _ in range(N+1)]


for _ in range(M):
    # 역방향도 넣어줘야 되낭
    s, e = map(int, input().split()) # 0부터가 아니라 1부터 시작임
    graph[s].append(e)
    graph[e].append(s)

for i in range(1, N+1):
    graph[i].sort()

# DFS 
# 1. 방문처리 & push
# 2. 스택 맨 위 애 중 방문 안 했으면서 가장 작은 애 추가
# 3. 스택 맨 위에 갈 곳이 없으면 pop


def dfs(graph, v, visited):
    visited[v] = True
    print(v, end=' ')

    for i in graph[v]:
        if visited[i] == False:
            dfs(graph, i, visited)


visited = [False] * (N+1)
dfs(graph, V, visited)




# BFS
# 1. 방문처리, 큐 추가
# 2. pop 하고 연결되었으면서 방문 X 애들 다 추가
print()
visited = [False] * (N+1)
def bfs(graph, v, visited):

    queue = [v]
    visited[v] = True

    while queue:
        i = queue.pop(0)
        print(i, end=' ')
        for j in graph[i]:
            if not visited[j]:
                queue.append(j)
                visited[j]=True
visited = [False] * (N+1)
bfs(graph, V, visited)

