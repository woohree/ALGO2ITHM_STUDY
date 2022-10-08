# import sys
# sys.stdin = open('input.txt')

import sys
# sys.stdin = open('input.txt')
a,b = map(int,sys.stdin.readline().split())

lanseon = []
for _ in range(a):
    lanseon.append(sys.stdin.readline())

sum = 0
for length in lanseon:
    sum += int(length)


maxlen = sum//b
answer = 0
cnt = 0
while answer == 0:
    for length in lanseon:
        cnt += (int(length) // maxlen)
    if cnt >= b:
        answer = maxlen
    maxlen -= 1
    cnt = 0
print(answer)