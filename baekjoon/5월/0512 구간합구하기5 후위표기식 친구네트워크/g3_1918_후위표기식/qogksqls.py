# 36 11:17
import operator
import sys
sys.stdin = open('B.txt')


def solution():
    global j
    f = 2
    count = 0

    while calculation[j] != ')':
        if calculation[j] == '(':
            j += 1
            solution()

        elif calculation[j] == '*':
            if f == 2:
                f = 1
            count += 1
            operations.append(calculation[j])
            f = 1

        elif calculation[j] == '/':
            if f == 2:
                f = 1
            count += 1
            operations.append(calculation[j])
            f = 1

        elif calculation[j] == '+':
            if f == 1:
                while operations[-1] == '*' or operations[-1] == '/':
                    new_calculation.append(operations.pop())
                    count -= 1
            elif f == 2:
                f = 0
            count += 1
            operations.append(calculation[j])
            f = 0

        elif calculation[j] == '-':
            if f == 1:
                while operations[-1] == '*' or operations[-1] == '/':
                    new_calculation.append(operations.pop())
                    count -= 1
            elif f == 2:
                f = 0
            count += 1
            operations.append(calculation[j])
            f = 0
        else:
            new_calculation.append(calculation[j])
        j += 1
    while count:
        new_calculation.append(operations.pop())
        count -= 1


calculation = list(sys.stdin.readline().rstrip())
new_calculation = []
operations = []
four_operations = ['+', '-', '*', '/']
temp = []
flag = 2
i = 0
while i < len(calculation):
    if calculation[i] == '(':
        solution()

    elif calculation[i] == '*':
        operations.append(calculation[i])
        i += 1
        temp.append(calculation[i])
        while operations:
            temp.append(operations.pop())
    elif calculation[i] == '/':
        operations.append(calculation[i])
        i += 1
        temp.append(calculation[i])
        while operations:
            temp.append(operations.pop())

    elif calculation[i] == '+':
        operations.append(calculation[i])
    elif calculation[i] == '-':
        operations.append(calculation[i])
    else:
        new_calculation.append(calculation[i])
    i += 1

print(''.join(new_calculation))
