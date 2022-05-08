import sys
input = sys.stdin.readline

N = int(input())
points = [list(map(int, input().split())) for _ in range(N)]

points = sorted(points, key = lambda x: (x[0], x[1]))

for p in points:
    print(p[0],p[1])
