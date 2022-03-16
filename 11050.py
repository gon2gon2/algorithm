N, K = map(int, input().split())

# 시도 1
# 틀렸습니다 -> 이렇게 푸는 게 아니었당
# def answer(N, K):
#     if N/2 < K:
#         K = N-K
#     return N*K


# 시도 2
# 팩토리얼 함수를 이용하고 f(n)/ (f(n-k) * f(k)))

def factorial(n):
    if n == 1 or n == 0:
        return 1
    return factorial(n-1) * n

def answer(N, K):
    return factorial(N) // (factorial(N-K) * factorial(K))

print(answer(N,K))

# print(answer(5, 0))
# print(answer(5, 1))
# print(answer(5, 2))
# print(answer(5, 3))
# print(answer(5, 4))
# print(answer(5, 5))

# print(answer(6, 0))
# print(answer(6, 1))
# print(answer(6, 2))
# print(answer(6, 3))
# print(answer(6, 4))
# print(answer(6, 5))
# print(answer(6, 6))