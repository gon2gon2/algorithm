'''
N의 분해합 -> N +  N[0] + N[1] + ...
256 = 245 + 2 + 4 + 5
245는 256의 생성자.


1. 1부터 올라간다

'''
import sys
N = int(sys.stdin.readline())

def get_answer(x):
    for i in range(N):
        x = i + sum(map(int,list(str(i))))
        if x == N:
            return i
    return 0

print(get_answer(N))