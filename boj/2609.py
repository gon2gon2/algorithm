import sys
import math
A, B = map(int, sys.stdin.readline().split())

def get_divisors(x: int): 
    divisors = {1, x}
    for i in range(2, int(math.sqrt(x))+1):
        if x %i == 0:
            divisors.add(i)
            divisors.add(x//i)

    return divisors


def get_answer(A, B):
    '''최소공배수
    A랑 B 둘 다 약수로 갖는 어떤 수를 찾아야 함
    A,B의 min을 구해서 1부터 곱하면서 둘다 나눴을 때 나머지가 0이면 ok
    '''
    mini = min(A,B)
    cnt = 0
    while True:
        cnt += 1
        standard = cnt * mini
        if standard%A == 0 and standard%B ==0:
            return mini * cnt
    



ans_1 = max(get_divisors(A) & get_divisors(B))
ans_2 = get_answer(A, B)

print(ans_1)
print(ans_2)