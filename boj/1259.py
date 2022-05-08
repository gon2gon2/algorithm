def check(x):
    stack = []
    length = len(x)
    middle = length//2
    if length <= 1:
        return "yes"

    elif length % 2 == 0: #짝수인 경우
        left, right = x[:middle], x[middle:]
    else:
        left, right = x[:middle], x[middle+1:]

    left = list(left)
    right = list(right)
    for r in right: # 문자열 순회하면서 append하다가 middle index랑 겹치면 그때부터 pop하는 걸로
        if left.pop() != r:
            return "no"
    return "yes"


    

while True:
    x = input()
    if x == '0':
        break
    else:
        print(check(x))


