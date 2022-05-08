'''
목표: 카드의 합을 최대로
양의 정수가 적힌 카드 N장을 뿌림

플레이어는 N에서 3개를 고르고, M보다 작거나 같게
'''

from itertools import combinations
import sys

N,M = map(int, sys.stdin.readline().split())
CARDS = map(int, sys.stdin.readline().split())
best = 0
for comb in combinations(CARDS, 3):
    new = sum(comb)
    if new == M:
        # M이랑 같으면 더 구할 것도 없으니 break
        # 그러나 시간 안 올랐음
        best = new
        break

    elif (new <= M) and (new > best):
        best = new

print(best)