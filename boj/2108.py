# input 대신 readline쓰니까 시간 초과 해결!

import sys
N = int(sys.stdin.readline())

numbers = sorted([int(sys.stdin.readline()) for i in range(N)])

total = sum(numbers)

# print("#########")
print(round(sum(numbers)/N))
print(numbers[N//2]) # 1,1,2,2,3,3,4    1,2,3,4,5

def get_mode(numbers: list):

    from collections import Counter
    most_common = Counter(numbers).most_common()

    if len(most_common) == 1:
        return numbers[0]

    else:
        if most_common[0][1] == most_common[1][1]:
            return max(most_common[0][0], most_common[1][0])

        return most_common[0][0]

print(get_mode(numbers))
print(numbers[-1] - numbers[0])

# TC 1
# 11
# 1,1,1,
# 2,2,
# 3,3,3,
# 4,4
# 5


# 2
# 2
# 2
# 3