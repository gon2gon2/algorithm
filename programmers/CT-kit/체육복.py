# 시작: 15:38
# 종료: 16:31

'''
메인 로직은 바로 구현했는데 교집합을 빼줘야 하는 부분이나 맨 앞에서부터 해야되는 부분 잡느라 시간이 오래 걸렸다.
'''


def solution(n, lost, reserve):
    intersection = set(lost) & set(reserve)
    lost = list(set(lost) - intersection)
    reserve = list(set(reserve) - intersection)
    
    while reserve:
        
        r = reserve.pop(0)
        
        if r in lost:
            lost.remove(r)
            
        elif r-1 in lost:
            lost.remove(r-1)
            
        elif r+1 in lost:
            lost.remove(r+1)
           
    return n - len(lost)
