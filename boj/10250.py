'''
N이 H의 배수인 경우를 고려하지 않아서 틀렸다.
'''
import sys
def alloc_room(H, W, N):
    num = N//H + 1
    floor = N%H
    if floor == 0:
        floor = H
        num -= 1
    return f"{floor*100 + num}"


T = int(sys.stdin.readline())
data = [map(int,sys.stdin.readline().split()) for _ in range(T)]

for [h, w, n] in data:
    print(alloc_room(h,w,n))

# 테스트케이스
# print(alloc_room(6, 12, 10))    # 402
# print(alloc_room(30,50,72))     # 1203
# print(alloc_room(6,12,1))       # 101
# print(alloc_room(6,12,2))       # 201
# print(alloc_room(6,12,3))       # 301
# print(alloc_room(6,12,4))       # 401
# print(alloc_room(6,12,5))       # 501
# print(alloc_room(6,12,6))       # 601
# print(alloc_room(6,12,12))       # 602
# print(alloc_room(6,12,18))       # 603
# print(alloc_room(6,12,24))       # 604
# print(alloc_room(6,12,7))       # 102
# print(alloc_room(6,12,27))      # 305
