n = int(input())
target = [int(input()) for _ in range(n)]

ns = list(range(1,n+1))
opers = []
stack = [-1]
while target:
    if target[0] == stack[-1]:
        # print("-")
        opers.append("-")
        target.pop(0)
        stack.pop()
        continue
    elif target[0] > stack[-1]:
        pass
    else:
        break

    stack.append(ns.pop(0))
    # print("+")
    opers.append("+")

# print(f"n:\t{n}")
# print(f"ns:\t{ns}")
# print(f"target:\t{target}")
if target:
    print("NO")
else:
    for oper in opers:
        print(oper)

'''
1부터 하나씩 뽑아서 target[0]이랑 비교해서 일단 한번 수행

1. 같은지 비교
    -1 stack[0]이랑 같으면 target.pop(0), continue
    -2 stack[0]이랑 작으면 pass
    -3 stack[0]이랑 크면 break
2. append
3. 



8
4
3
6
8
7
5
2
1
'''