'''
(x,y), (p,q)
x>p, y>q

# 키와 몸무게를 따로 분리
# max(key)


1. max_height과 max_weight을 각각 찾는다
2. 같으면 hash[now_rank].append(일치하는 인덱스)
3. 다르면 height이나 weight이 max보다 큰 애들하나씩 append(if, elif ---- 한번만 추가되게) hash[now_rank].append(현재 인덱스)




'''

# from collections import namedtuple, defaultdict

# # person = namedtuple("person", "weight height ranked")

# rank_table = defaultdict(list)

# N = 5
# people = [
#     person(55, 185, False),
#     person(58, 183, False),
#     person(88, 186, False),
#     person(60, 175, False),
#     person(46, 155, False),
#     ]

# max_height_idx = 0 # 초기화 하기 힘드네
# max_weight_idx = 0 
# now_rank = 1
# cnt = 0

# while cnt != N:
    
#     for idx in range(N):
#         if people[idx].ranked:
#             continue

#         if people[idx].height > people[max_height_idx].height:
#             max_height_idx = idx
        
#         if people[idx].weight > people[max_weight_idx].weight:
#             max_weight_idx = idx

#     if max_height_idx == max_weight_idx:
#         rank_table[now_rank].append(max_height_idx)
#         cnt += 1
#     else:
#         for idx in range(N):
#             if people[idx].ranked:
#                 continue
#             if people[idx].height > people[max_height_idx].height \
#                 or people[idx].weight > people[max_height_idx].weight:
#                 rank_table[now_rank].append(idx)
#                 cnt += 1


## 방법 2 땡!!!
# people = [
#     [55, 185, False],
#     [58, 183, False],
#     [88, 186, False],
#     [60, 175, False],
#     [46, 155, False],
#     ]

# import sys
# N = int(sys.stdin.readline())
# people = [[*map(int, sys.stdin.readline().split()), False] for _ in range(N)]

# cnt = 0
# while cnt != N:
#     max_height = -99
#     max_weight = -99 
#     now_rank = cnt + 1
    
#     for idx, [w, h, r] in enumerate(people):
#         if r: continue

#         if h > max_height:
#             max_height = h
#             max_height_idx = idx
        
#         if w > max_weight:
#             max_weight = w
#             max_weight_idx = idx

#     if max_height_idx == max_weight_idx:
#         people[max_height_idx][2] = now_rank
#         cnt += 1
#     else:
#         for idx, [w, h, r] in enumerate(people):
#             if r : continue
#             # 제일 큰 애보다 몸무게가 나가거나
#             # 제일 무거운 애보다 키가 크거나
#             if w > people[max_height_idx][0] or h> people[max_weight_idx][1]:
#                 people[idx][2] = now_rank
#                 cnt += 1

# for p in people:
#     print(p[-1], end=' ')


# 브루트 포스: 나보다 확실히 큰 애만 찾으면 된다고 한다.
import sys
N = int(sys.stdin.readline())
people = [[*map(int, sys.stdin.readline().split())] for _ in range(N)]

# people = [
#     [55, 185, False],
#     [58, 183, False],
#     [88, 186, False],
#     [60, 175, False],
#     [46, 155, False],
#     ]

for i in people:
    rank = 1
    for j in people:
        if i[0] < j[0] and i[1] < j[1]:
            rank += 1
    print(rank, end=' ')