'''
1. input: 원하는 높이, 땅
2. output: 시간

높이를 기준으로 뺄 건 빼고 더할 건 더하고 -> 필요한 블럭 수, 인벤토리 수


'''

# import sys;input = sys.stdin.readline

# n, m, b = map(int, input().split())

# land = []
# for _ in range(n):
#     row = list(map(int,input().split()))
#     land += row

# def make_land(land, level, b):
#     # block_calc = list(map(lambda x:x-level, land))
#     # map 결과가 양수 -> 제거할 블럭 -> 2초
#     # map 결과가 음수 -> 추가할 블럭 -> 1초

#     # 음수 * 1
#     # 양수 * 2
#     block_calc = list(map(lambda x:x-level, land))
#     block_remove = 0
#     block_add = 0
#     for block in  block_calc:
#         if block > 0:
#             block_remove += 1
#         elif block < 0 :
#             block_add += 1
    
#     # block_remove = abs(sum(filter(lambda x: x>0, block_calc)))
#     # block_add = abs(sum(filter(lambda x: x<0, block_calc)))

#     if block_add <= (block_remove + b):
#         return block_remove * 2 + block_add * 1


#     return False


# best_sec = 9999999999999
# for level in range(max((0, min(land))),min(max(land)+1, 256)):
#     false_or_sec = make_land(land, level, b)
#     if false_or_sec and false_or_sec < best_sec:
#         answers = []
#         best_sec = false_or_sec
#         answers.append(level)
#     elif best_sec == false_or_sec :
#         answers.append(level) 
    
# print(best_sec, max(answers))




from math import inf
import sys;input = sys.stdin.readline

n, m, b = map(int, input().split())

land = []
for _ in range(n):
    row = list(map(int,input().split()))
    land += row

answer = inf
h = 0
for level in range(257):
    need = 0
    not_need = 0
    for block in land:
        block = block - level

        if block > 0: # 원하는 층보다 높아서 빼야돼
            not_need += block
        elif block < 0: # 원하는 층보다 낮아서 더해줘야돼
            need += -block

    if need > b + not_need: # 필요한 블럭 수
        continue


    sec = not_need * 2 + need * 1

    if sec <= answer:
        h = level
        answer = sec

print(answer, h)