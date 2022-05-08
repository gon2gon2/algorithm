class Deque:
    def __init__(self):
        self.data = []

    def push_front(self, x):
        self.data.insert(0,x)

    def push_back(self,x):
        self.data.append(x)

    def pop_front(self):
        try:
            print(self.data.pop(0))
        except:
            print(-1)
    def pop_back(self):
        try:
            print(self.data.pop(-1))
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

deque = Deque()
for cmd in cmds:
    if cmd[0] == "push_front":
        deque.push_front(cmd[1])
    elif cmd[0] == "push_back":
        deque.push_back(cmd[1])
    elif cmd[0] == "pop_front":
        deque.pop_front()
    elif cmd[0] == "pop_back":
        deque.pop_back()
    elif cmd[0] == "size":
        deque.size()
    elif cmd[0] == "empty":
        deque.empty()
    elif cmd[0] == "front":
        deque.front()
    elif cmd[0] == "back":
        deque.back()