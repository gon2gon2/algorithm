'''
소괄호
대괄호

왼쪽 기호는 push 오른쪽 기호는 pop
다 끝났을때 stack에 남아있으면 no 아니면 yes

비정상적인 경우
1. 스택이 없는데 닫는 괄호가 나왔을 때
2. )가 나왔는데 ]가 나오거나 ]가 나왔는데 (가 나오거나

조건문을
    1. ( or [
    2. ) or ]
로 해서 보기 안 좋다

1.(
2.)
3.[
4.]
로 하면 더 명확할듯
'''


def answer(chars: str):
    stack = []
    dict_ = {
        "(" : ")",
        "[" : "]"
        }
    for c in list(chars):
        if c == "(" or c =="[":
            stack.append(c)
        elif c == ")" or c =="]":
            if not stack:
                return "no"
            pop = stack.pop()
            if dict_[pop] == c:
                continue
            else:
                return "no"
    
    return "no" if stack else "yes"
string = input()
while string != ".":
    print(answer(string))
    string = input()

# 테스트케이스
# print(answer('''So when I die (the [first] I will see in (heaven) is a score list).'''))
# print(answer('''[ first in ] ( first out ).'''))
# print(answer('''Half Moon tonight (At least it is better than no Moon at all].'''))
# print(answer('''A rope may form )( a trail in a maze.'''))
# print(answer('''Help( I[m being held prisoner in a fortune cookie factory)].'''))
# print(answer('''([ (([( [ ] ) ( ) (( ))] )) ]).'''))
# print(answer(''' .'''))
# print(answer('''.'''))