from collections import deque
def solution(queue1, queue2):
    answer = 0
    sum1 = sum(queue1)
    sum2 = sum(queue2)
    
    mid = sum1 + sum2
    if mid % 2: return -1
    
    queue1 = deque(queue1)
    queue2 = deque(queue2)
    
    # 반반 나눠서 
    while sum1 != sum2 and answer < (len(queue1) + len(queue2)) + 2:
        answer += 1
        if sum1 > sum2:
            x = queue1.popleft()
            queue2.append(x)
            sum1 -= x
            sum2 += x
        else:
            x = queue2.popleft()
            queue1.append(x)
            sum2 -= x
            sum1 += x

    return answer if sum1 == sum2 else -1