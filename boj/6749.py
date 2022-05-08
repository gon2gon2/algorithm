import sys
ages = []
for _ in range(2):
    ages.append(int(sys.stdin.readline()))
print(ages[-1] + ages[-1] - ages[-2])
