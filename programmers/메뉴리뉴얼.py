from collections import Counter
from itertools import combinations

def solution(orders, course):
    answer = []
    
    for c in course:
        temp = []
        
        for order in orders:
            # order를 c개수로 combination화 한 다음, 한 곳에 모아 counter로 세준다.
            temp += list(combinations(sorted(order), c))
        counter = Counter(temp)
        
        if counter and counter.most_common(1)[0][-1] > 1:
            most = max(counter.values())
            answer += [''.join(sorted(k)) for k, v in counter.items() if v == most]
        
    return sorted(answer)