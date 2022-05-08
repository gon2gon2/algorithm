'''
절단기에 H 지정
그럼 모든 나무에 대해 H로 자르는데 짧으면 안 잘림
all trees <= H

자르고 나서 양수인 것만 합쳤을 떄 목표라 같으면 ok

나의 접근: 큰 나무 길이부터 잘라보기(브루트 포스) -> 시간 초과
이분 탐색, 그러나 최대한 큰 값을 찾아야 하므로 조건을 두개로 간소화
같다 조건을 제외
마지막 시도를 했을 때 오바되면 이전의 값을 써야 하므로 right를 출력

'''

import sys

N,M = map(int, sys.stdin.readline().split())
TREES = list(map(int, sys.stdin.readline().split()))

left, right = 0, max(TREES)

while left <= right:
    h = (left + right)//2
    total = sum([(tree-h) for tree in TREES if tree>h])
    if total >= M: # 많이 남음
        left = h + 1
    elif total < M: # 작어 
        right = h - 1

print(right)