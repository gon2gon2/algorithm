import sys
total = 0
for _ in range(4):
    n = int(sys.stdin.readline())
    total += n 
print(total//60)
print(total%60)