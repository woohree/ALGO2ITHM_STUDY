# 백준 1347 미로 만들기 S4 문제
# 2:24 시작 3:36 알고리즘 고민중

import sys
sys.stdin = open('input.txt')

N = int(input())
strings = list(''.join(input()))  # 둘째 줄을 리스트로 받음

direction = [  # 동서남북을 이차리스트로 표현
    [0, 1, 0],
    [1, 0, 1],
    [0, 1, 0],
]
current_direction = direction[2][1]
for string in strings:
    if string == 'R':
        current_direction = direction[]
    if string == 'L':
        pass
    if string == 'F':
        pass


print(string)