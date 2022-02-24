import sys
from collections import deque
# n = int(sys.stdin.readline())
n=4
# for n in range(1,10):
    # print("###########")
    # print(n)
    # card_q = deque(range(2,n+1,2))
card_q = deque(range(1,n+1))


while len(card_q) > 1:
    bye = card_q.popleft()
    back = card_q.popleft()
    card_q.append(back)

print(card_q[0] if card_q else 1)

    # if (n % 2 != 0) & (n>2):
    #     '''append부터 시작'''
    #     card_q.append(card_q.pop(0))

    # print("시작: ", card_q)
# 1,2,3,4,5,6
# 23456 34562
# 4562  5624
# 562   625
# 


'''

1 -> 1
1 2 -> 2
1 2 3 -> 2 3, 3 2 -> 2
1 2 3 4 -> 2343424224 4


1234
234     342
42      24
4


1234

234     342
42      24
4



12345  홀 -> append부터
        짝 -> pop부터

2345    3452
452     524
24      42
2



1234567
234567  345672
45672   56724
6724    7246
246     462
62      26
6



123456

23456   34562
4562    5624
624     246
46      64
4

'''