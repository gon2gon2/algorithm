from math import sqrt
def is_prime(x):
    if not x or x < 2:
        return False
    for i in range(2, int(sqrt(x))+1):
        if x % i == 0:
            return False
    return True

def convert(n, q):
    rev_base = ''
    
    while n > 0:
        n, mod = divmod(n, q)
        rev_base += str(mod)
    return rev_base[::-1]
    
def solution(n, k):
    answer = 0
    sp = convert(n,k).split('0')
    
    for s in sp:
        if s != '' and is_prime(int(s)):
            print(s)
            answer += 1
    return answer
