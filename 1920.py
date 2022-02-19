n = int(input())
ns = map(int,input().split())
m = int(input())
ms = map(int,input().split())
ns = sorted(ns)

for target in ms:
    left, right = 0, len(ns)-1

    while (left <= right):
        mid = (left + right)//2
        
        if ns[mid] > target:
            right = mid - 1
        elif ns[mid] < target:
            left = mid + 1
        else:
            break

    print(1 if ns[mid] == target else 0)

    

# print(n,ns,m,ms)


"""
ms에서 하나씩 꺼내가지고 이분탐색?


"""