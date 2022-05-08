# 시작: 21:55
# 종료: 22:20

'''
백준에서 풀었던 문제라 쉽게 풀었다.
20번 케이스의 경우는 '11111','2' 같은 중복된 숫자 case다.
해당 케이스를 떠올리느라 오래 걸렸다.
'''

def solution(number, k):
    stack = []
    length = len(number)
    answer_length = length - k
    cnt = k
    
    for idx in range(length):
        while stack and cnt and stack[-1] < number[idx] and len(stack) + length - idx > answer_length:
            stack.pop()
            cnt -= 1
        stack.append(number[idx])
    
    
    return "".join(stack[:answer_length])
