from itertools import combinations
import sys
sys.stdin = open('M.txt')

# 문제 개수 N, L <= 난이도 합 <= R, 가장 어려운 문제와 가장 쉬운 문제의 난이도 차 >= X
N, L, R, X = map(int, sys.stdin.readline().split())
A = list(map(int, sys.stdin.readline().split()))
answer = 0

for i in range(2, N + 1):
    combs = list(combinations(A, i))        # 모든 i개의 문제 조합

    for comb in combs:
        max_level, min_level = max(comb), min(comb)
        if max_level - min_level >= X and L <= sum(comb) <= R:
            answer += 1

print(answer)
