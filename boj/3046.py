# R1, S -> R2

# (R1 + R2)= S * 2 - R1

import sys
R1, S = map(int, sys.stdin.readline().split(' '))
R2 = S * 2 - R1
print(R2)
