class Stack:
    def __init__(self):
        self.data = []

    def push(self, x):
        self.data.append(x)
    
    def pop(self):
        if self.data == []:
            print(-1)
        else:
            print(self.data.pop())
        
    def size(self):
        print(len(self.data))
        
    def empty(self):
        print(int(self.data == []))
         
    def top(self):
        if self.data == []:
            print(-1)
        else:
            print(self.data[-1])
         

import sys
input = sys.stdin.readline
stack = Stack()

N = int(input())
cmds = [input().split() for _ in range(N)]

for cmd in cmds:
    if cmd[0] == 'push':
        stack.push(cmd[1])
    elif cmd[0] == 'top':
        stack.top()
    elif cmd[0] == 'size':
        stack.size()
    elif cmd[0] == 'empty':
        stack.empty()
    elif cmd[0] == 'pop':
        stack.pop()