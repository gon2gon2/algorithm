# N, r, c = map(int, input().split())


# def get_start_point(N, r, c):

#     if N == 1:
#         return 0

#     center = 2**(N-1)

#     # 0
#     if r < center and c < center:
#         return 0 + get_start_point(N-1, r, c)

#     # 1
#     elif r >= center and c < center:
#         return center ** 2 + get_start_point(N-1, r - center, c)

#     # 2
#     elif r < center and c >= center:
#         return center ** 2 *2 + get_start_point(N-1, r, c-center)

#     # 3
#     elif r >= center and c >= center:
#         return center ** 2 *3 + get_start_point(N-1, r - center, c-center)

# print(get_start_point(2,3,1))



# N, r, c = map(int, input().split())

# def answer(N, r, c):
#     ans = 0

#     while N != 0:
#         N -= 1


#         center = 2**N

#         # 0
#         if r < center and c < center:
#             ans += 0 

#         # 1
#         elif r < center and c >= center:
#             ans += (center ** 2)
#             c -= center

#         # 2
#         elif r >= center and c < center:
#             ans += (center ** 2) *2 
#             r -= center
#         # 3
#         elif r >= center and c >= center:
#             ans += (center ** 2) *3 
#             r -= center
#             c -= center


#     return ans

N, r, c = map(int, input().split())
def answer(N, r, c):
    if N == 0:
        return 0
    return 2*(r%2)+(c%2) + 4*answer(N-1, r//2, c//2)

print(answer(N,r,c))