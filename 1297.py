# TV의 대각선 길이 D, TV의 높이 비율 H, TV의 너비 비율 W
import math
D, H, W = map(int, input().split())
R = D / (H**2 + W**2) ** (1/2)
print(math.floor(R*H), math.floor(R*W))