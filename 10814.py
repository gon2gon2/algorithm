import sys
N = int(sys.stdin.readline())
people = [[*sys.stdin.readline().split(),i] for i in range(N)]
people = sorted(people, key=lambda x: (int(x[0]), int(x[2])))

for p in people:
    print(p[0], p[1])
