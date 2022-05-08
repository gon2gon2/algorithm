'''
1
7
20
37
61

6, 13, 17, 24
1
2~7     6
8~19    12
20~37   18
38~61   24
'''
import sys
N = int(sys.stdin.readline())

ans = 0
end = 1
for i in range(1,N):
    start = end + 1
    end = end + 6*i
    if start <= N  <= end :
        ans = i+1
        break 
print(ans if ans else 1)