'''
뭐지, DP인가 brute force인가
소수: 자신이랑 1 밖에 나눌 수가 없는 수, 나머지는 나머지가 생긴다.

m부터 1씩 올라가면서 n에 도달할 때 까지
n까지 소수를 구해가면서 +1로 나누지말고 

'''
import sys
import math
m,n = map(int, sys.stdin.readline().split())

# 방법 2
# 2부터 n까지 소수를 찾아가면서 넣는다.
# n까지 가는 길은 소수로 나누면서 간다.


def get_sosu(x):
    for i in range(2, int(math.sqrt(x))+1):
        if x%i == 0: 
            return False
    return True

import time
s = time.time()
for x in range(2, n+1):
    if (get_sosu(x)) & (m<=x<=n):
        print(x)
e = time.time()
print(e-s)