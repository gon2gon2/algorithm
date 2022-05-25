# 정렬시켜놓고 deque에서 맨 오른쪽+ 맨왼쪽 했을 떄 괜찮으면 continue
# 아 최대 2명밖에 못타는 걸 다 풀고 나서 알았다.
from collections import deque
def solution(people, limit):
    answer = 0
    people.sort()
    
    people_queue = deque(people)
    remain = limit
    
    while people_queue:
        
        if people_queue[-1] <= remain:
            
            remain -= people_queue.pop()
            
        elif people_queue[0] <= remain:
            remain -= people_queue.popleft()
            
        else:
            answer += 1
            remain = limit
            
    if remain != limit:
        answer += 1
    
    
    return answer
