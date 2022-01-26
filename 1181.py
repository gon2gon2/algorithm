lst = []
for i in range(int(input())):
    lst.append(input())

sorted_list = sorted(set(lst), key= lambda x:(len(x), *[i for i in list(x)]))
for i in sorted_list:
    print(i)