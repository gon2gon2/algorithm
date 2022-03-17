R = 31
M = 1234567891

alphabet = "abcdefghijklmnopqrstuvwxyz"
table = {}
for v, k in enumerate(alphabet):
    table[k] = v+1


def answer(some_string):
    hap = 0
    for i, c in enumerate(some_string):
        hap += table[c] * R**i
    return hap%M
L = input()
some_string = input()
print(answer(some_string))
# print(answer("abcde") == 4739715)
# print(answer("zzz") == 25818)
# print(answer("i") == 9)
