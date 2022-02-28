'''
3층: 1호, 2호, 3호, ...
2층: 1호, 2호, 3호, ...
1층: 1호, 2호, 3호, ...
0층: 1호, 2호, 3호, ...

(a,b) == (a-1, 1), (a-1, 2), ...(a-1, b)

1,3,6,10,15, ..., 
1,2,3,4,5,6, ... ,b 명


1 [1,sum(list[k-1][:i])]


1 [1,3]
0 [1,2,3,4,5,...,b]

'''


# import 
# T = 2
# K, N = 1, 3

T = int(input())

for t in range(T):
    K = int(input())
    N = int(input())
    apartment = [[n for n in range(1,N+1)]]
    for k in range(1, K+1):
        apartment.append([sum(apartment[k-1][:i+1]) for i in range(N)])
    print(apartment[K][N-1])