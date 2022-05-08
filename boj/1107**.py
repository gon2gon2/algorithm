# N = int(input()) # 이동하려는 채널, target
# M = int(input()) # 고장난 버튼 개수
# # M = 35
# broken_buttons = input().split()# 누를 수 없는 버튼


# '''
# +,-로 이동할 수 있는 범위,

# 현재 채널 i가 가능한 조합인지 확인하고 가능하면 거기서 +- 몇개인지 계산

# 이런 형태의 if else는 처음 본다.
# 다 돌고 났는데도 안 걸린다면 else:로 보내는 코드
#     if 조건:
#         break
# else:

# 브루트포스 -> 일단 for문 쓰고 어떤 식으로 체크할지 생각하기
# '''

# ans = abs(N-100)

# for i in range(1000000):

#     for c in str(i):
#         if c in broken_buttons:
#             break
#     else:
#         ans = min(ans, abs(i-N)+len(str(i)))

# print(ans)












target = int(input()) # M
n_of_brokens = int(input())
if n_of_brokens:
    brokens = input().split()
else:
    brokens = []

cnt = abs(target - 100)

for channel in range(1000000):
    
    for c in list(str(channel)):
        if c in brokens:
            break
    else:
        cnt = min(cnt, len(str(channel)) + abs(target-channel))

print(cnt)






















