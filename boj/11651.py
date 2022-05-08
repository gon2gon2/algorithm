import sys; input = sys.stdin.readline

N = int(input())
points = [list(map(int,input().split())) for _ in range(N)]
for p in sorted(points, key= lambda x: (x[1], x[0])):
    print(p[0], p[1])