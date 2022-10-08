# 30분
import sys, math
from collections import deque
sys.stdin = open('B.txt')

N = int(input())
K = int(math.log2(N // 3))

top = '  *  '
middle = ' * * '
bottom = '*****'
result = deque()
result.append(bottom)
result.append(middle)
result.append(top)

while K >= 1:
    len_result = len(result)
    for r in range(len_result):
        result.append('   ' + result[r] + '   ')
    for r in range(len_result):
        for _ in range(2 ** K - 1):
            result[r] += ' ' + result[r]
    K -= 1

for r in range(N-1, -1, -1):
    print(result[r])
