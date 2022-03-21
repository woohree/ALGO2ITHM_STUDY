# 20분

import sys
sys.stdin = open('B.txt')

from itertools import permutations

N, K = map(int, input().split())
exercise_kit = list(map(int, input().split()))

# 순열 생성
perm = list(permutations(exercise_kit, N))

# count에 순열의 개수 저장.
count = len(perm)
for p in perm:
    five_hundreds = 500
    for i in range(len(p)):
        five_hundreds += p[i] - K
        # 조건이 불만족 할 때마다 count에서 1 뺌
        if five_hundreds < 500:
            count -= 1
            break

print(count)
