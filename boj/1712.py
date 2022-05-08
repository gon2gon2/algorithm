FC, VC, P = map(int, input().split())

income_per_sold = P-VC # 이게 0 이하면 -1

# FC를 income_per_sold로 나눴을 때의 값을 return

def get_point(FC, VC, P):
    if income_per_sold <= 0:
        return -1
    return int(FC/(P-VC) + 1)

print(get_point(FC, VC, P))