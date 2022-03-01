N = int(input())

# def answer(N):
#     '''
#     그리디로 접근.
#     그러나 5의 몫을 일부 양보함으로서 수를 딱 맞출 수 있는 경우를 고려하지 못함.
#     '''
#     bags = 0
#     quotient, remainder = divmod(N, 5)
#     bags += quotient

#     if (remainder%3 == 0) :
#         # 나머지가 0이면 bags에 remainder 더해
#         bags += remainder//bags

#     else:
#         # 나머지가 있으면
#         if (N % 3) == 0:
#             # 나머지가 있지만 3으로 딱 맞출 수 있는 경우
#             bags = N//3

#         else:
#             # 못 맞춤 ㅈㅈ
#             bags = -1

#     return bags

def answer(N):
    bags = 999999999

    for i in range(N//5 + 1):
        if (N - 5*i)%3 == 0:
            bags = min(bags, i + (N-5*i)//3)

    return bags if bags != 999999999 else -1
print(answer(N))
# 테스트 케이스
# print(answer(18) == 4)
# print(answer(4) == -1)
# print(answer(6) == 2)
# print(answer(9) == 3)
# print(answer(11) == 3)
