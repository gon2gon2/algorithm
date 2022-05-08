'''
N개의 랜선을 만들 수 있는 최대 길이
오영식은 길이가 다른 K개의 랜선을 가지고 있다.

Ks를 어떤 단위로 나눴을 때, N개를 넘으면 되는데, 이때 Ks의 최댓값

Ks의 최솟값부터 -1하면서 몫만 구해서 더해가지고 넘으면 print()

기존의 K개의 랜선으로 N개의 랜선을 만들 수 없는 경우는 없다

# 만약 이미 가지고 있는 게(K) 훨씬 많으면?
3, 2
900 800 300
Ks[K-1]
'''
import sys

K, N = map(int, sys.stdin.readline().split())
lines = sorted([int(sys.stdin.readline()) for _ in range(K)])

start, end = 1, lines[-1] # 탐색할 값의 범위

while start <= end:

    mid = (start + end)//2
    cnt = sum([line//mid for line in lines])

    if cnt >= N:
        start = mid + 1
    else:
        end = mid - 1
print(end)
