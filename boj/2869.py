from sys import stdin
A, B, V = map(int, stdin.readline().split())


def answer(A, B, V):
    '''
    일단 A를 주고
    A-B를 계속 더해주면서 확인

    or

    A를 주고 A-B로 나눈 다음 나머지가 있으면 N+1
    '''
    h_now = A
    days = 1
    h_per_day = A-B

    # 방법 1
    # 개오래걸림
    # while h_now < V:
    #     h_now = h_now + (h_per_day)
    #     days += 1
    # return days

    # 방법 2
    quotient, remainder = divmod((V-A), (h_per_day))
    if remainder:
        quotient += 1
    days += quotient
    return days

print(answer(A, B, V))

# 테스트 케이스
# print(answer(2, 1, 5) == 4)
# print(answer(5, 1, 6) == 2)
# print(answer(100, 99, 1000000000) == 999999901)
