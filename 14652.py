import sys
N, M, K = map(int,sys.stdin.readline().split())
print(K//M, K%M)

# 메모리 초과
# import sys
# N, M, K = map(int,sys.stdin.readline().split())
# seats = [[n,m] for n in range(N) for m in range(M)]
# print(*seats[K])

