'''
1번부터 N번의 사람.


'''
# N, K = 7, 3

N, K = map(int,input().split())

members = [i+1 for i in range(N)]
out = []
cnt = 0
while members:
    cnt += 1
    m = members.pop(0)
    if cnt == K:
        out.append(m)
        cnt = 0
        continue
    else:
        members.append(m)

print(f"<{', '.join(map(str,out))}>")