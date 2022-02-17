# 8:20
# 시리얼 번호는 알파벳 대문자 (A-Z)와 숫자 (0-9)로 이루어져 있다.
# 1. A와 B의 길이가 다르면, 짧은 것이 먼저 온다.
# 2. 길이가 같다면, 모든 자리 수의 합을 비교해서 작은 합을 가지는 것이 먼저 온다. (숫자인 것만 더한다)
# 3. 만약 1,2번 둘 조건으로도 비교할 수 없으면, 사전순으로 비교한다. 숫자가 알파벳보다 사전순으로 작다.
# N <= 50

# 저 세가지 조건을 만족하려면 3-1-2 순으로 조건을 설정하는 것이 바람직
# 사전순 정렬을 마지막으로 하면 1,2조건으로 정렬했던것이 다시 섞일 위험이 있기 때문

import sys
sys.stdin = open('input.txt')

N = int(input())
serial_numbers = [input() for _ in range(N)]

# 숫자들만의 total을 비교하는 함수~
def compare_total(a, b):
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    a_sum = 0
    for j in list(a):
        if j in numbers:
            a_sum += int(j)

    b_sum = 0
    for j in list(b):
        if j in numbers:
            b_sum += int(j)

    if a_sum > b_sum:
        return b
    elif a_sum < b_sum:
        return a


# 세 번째 조건
for k in range(len(serial_numbers)):
    for i in range(len(serial_numbers) - 1, 0, - 1):  # 내림차순으로 내려옴
        if serial_numbers[i] < serial_numbers[i - 1]:
            temp = serial_numbers[i]
            serial_numbers[i] = serial_numbers[i - 1]
            serial_numbers[i - 1] = temp
# 첫 번째 조건
for k in range(len(serial_numbers)):
    for i in range(len(serial_numbers) - 1, 0, -1):
        if len(serial_numbers[i]) < len(serial_numbers[i - 1]):
            temp = serial_numbers[i - 1]
            serial_numbers[i - 1] = serial_numbers[i]
            serial_numbers[i] = temp
# 두 번째 조건
for k in range(len(serial_numbers)):
    for i in range(len(serial_numbers) - 1, 0, - 1):
        if len(serial_numbers[i]) == len(serial_numbers[i - 1]):
            c = compare_total(serial_numbers[i], serial_numbers[i - 1])
            if c == serial_numbers[i]:  # 작은 값을 앞으로 보냄
                temp = serial_numbers[i]
                serial_numbers[i] = serial_numbers[i - 1]
                serial_numbers[i - 1] = temp

for serial_number in serial_numbers:
    print(serial_number)
