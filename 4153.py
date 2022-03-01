from math import sqrt

def answer(A, B, C):

    [A1, A2, H] = sorted([A,B,C])
    if sqrt(A1**2 + A2**2) == H:
        return "right"
    return "wrong"




A, B, C = map(int, input().split())

while (A!=0) and (B!=0) and (C!=0):
    print(answer(A, B, C))
    A, B, C = map(int, input().split())