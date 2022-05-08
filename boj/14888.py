from itertools import permutations
from typing import MutableSequence


def answer(N: int, number: MutableSequence, operator: MutableSequence) :

    operator = ["+"] * operator[0] + ["-"] * operator[1] + ['*'] * operator[2] + ['/'] * operator[3]

    print('연산자:',operator)
    최댓값 = 0
    최솟값 = 1000000001

    number_zip = number[1:]
    for oper_zip in permutations(operator, len(operator)):
        value = number[0]
        for n, o in zip(number_zip, oper_zip):

            if o == "+":
                value += n
            elif o == "-":
                value -= n
            elif o == "*":
                value *= n
            else:
                if value < 0 :
                    value = -((-value)//n)
                else:
                    value = value //n

        if value > 최댓값:
            최댓값 = value

        if value < 최솟값:
            최솟값 = value

    return 최댓값, 최솟값


# N = int(input())
# numbers = list(map(int, input().split()))
# operators = list(map(int, input().split()))

# answers = answer(N,numbers,operators)
# print(answers[0])
# print(answers[1])



N_input = [2,3,6]
number_input = [
    [5,6],
    [3,4,5],
    [1,2,3,4,5,6]
]
operator_input = [
    [0,0,1,0],
    [1,0,1,0],
    [2,1,1,1],
]
answers = [
    [30,30],
    [35,17],
    [54,-24]
]

for i,(_1,_2,_3) in enumerate(zip(N_input, number_input, operator_input)):
    print(answer(_1,_2,_3))
    # print(answers[i])
    # print(answer(_1,_2,_3) == answers[i])
