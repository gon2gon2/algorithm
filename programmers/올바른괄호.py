'''
여는 괄호 -> append
닫는 괄호 pop한다
    1. 비어있는 경우 -> false
    2. 있는 경우
        2-1. 닫는 괄호가 나옴 -> false
        2-2. 여는 괄호 -> continue
'''
def solution(string):
    answer = True
    
    stack = []
    
    for s in string:
        if s == '(':
            stack.append('(')
        else:
            if not stack: return False
            top = stack.pop()
            if top == ')':
                return False

    return False if stack else True