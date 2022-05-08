N = int(input())


def check(chars):
    stack = []
    answer = {
        ")" : "(",
        "]" : "[",
    }
    for char in list(chars):
        if char == "(" or char=="[":
            stack.append(char)

        elif char == ')' or char == ']':
            if not stack:
                return "NO"
            popped = stack.pop()
            if popped != answer[char]:
                return "NO"

    return "YES" if not stack else "NO"

for _ in range(N):
    print(check(input()))


# 테스트 케이스
# print(check("(())())")=="NO")
# print(check("(((()())()")=="NO")
# print(check("(()())((()))")=="YES")
# print(check("((()()(()))(((())))()")=="NO")
# print(check("()()()()(()()())()")=="YES")
# print(check("(()((())()(")=="NO")
# print(check("((")=="NO")
# print(check("))")=="NO")
# print(check("())(()")=="NO")