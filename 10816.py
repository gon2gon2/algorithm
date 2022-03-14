import sys
from collections import Counter
N = int(sys.stdin.readline())
counter = Counter(sys.stdin.readline().split())
M = int(sys.stdin.readline())
for k in sys.stdin.readline().split():
    print(counter[k], end=' ')