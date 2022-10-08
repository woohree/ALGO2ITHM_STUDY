import sys
from itertools import combinations
sys.stdin = open('B.txt')

N, L, R, X = map(int, sys.stdin.readline().rstrip().split())
level = list(map(int, sys.stdin.readline().rstrip().split()))

count = 0
for i in range(2, N+1):
    comb = list(combinations(level, i))
    for c in comb:
        if L <= sum(c) <= R and max(c) - min(c) >= X:
            count += 1
print(count)
