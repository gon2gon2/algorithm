'''
1 -> 666
2 -> 1666
3 -> 2666
6 -> 5666
'''
n = int(input())

i = 0
n_th = 0
while True:
    i += 1
    if '666' in str(i):
        n_th += 1
    if n_th == n:
        print(i)
        break