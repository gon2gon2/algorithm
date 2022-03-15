class Queue:
    def __init__(self):
        self.data = []

    def push(self,x):
        self.data.append(x)

    def pop(self):
        try:
            print(self.data.pop(0))
        except:
            print(-1)

    def size(self):
        print(len(self.data))

    def empty(self):
        print(int(self.data == []))

    def front(self):
        try:
            print(self.data[0])
        except:
            print(-1)
    def back(self):
        try:
            print(self.data[-1])
        except:
            print(-1)

import sys
input = sys.stdin.readline

N = int(input())
cmds = [input().split() for _ in range(N)]

q = Queue()

for cmd in cmds:
    if cmd[0] == "push":
        q.push(cmd[1])
    elif cmd[0] == "pop":
        q.pop()
    elif cmd[0] == "size":
        q.size()
    elif cmd[0] == "empty":
        q.empty()
    elif cmd[0] == "front":
        q.front()
    elif cmd[0] == "back":
        q.back()
