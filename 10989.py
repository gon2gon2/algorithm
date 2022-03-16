import sys


N = int(sys.stdin.readline())

# 시도 1
# 평범한 방법 -> 메모리 초과
# 이유: append 사용시 메모리 resizing하느라 메모리 사용량이 2배가 되기도 하고 그렇다고 한다. from stackoverflow
# for i in sorted([int(sys.stdin.readline()) for _ in range(N)]):
#     print(i)


# 정답
# 문제에서 1~ 10,000의 숫자만 들어온다고 한다. 미리 그 개수만큼 원소를 만들어놓고 사용한다

numbers = [0] * 100001 # 인덱싱의 편의를 위해 10001
for i in range(N):
    n = int(sys.stdin.readline())
    numbers[n] += 1

for i in range(len(numbers)):
    if numbers[i] != 0:
        for j in range(numbers[i]):
            print(i)