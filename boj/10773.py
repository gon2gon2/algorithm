import sys
K = int(sys.stdin.readline())
stack = []
for _ in range(K):
    n = int(sys.stdin.readline())
    if n:
        stack.append(n)
    else:
        stack.pop()
print(sum(stack))