# 단순한 확률?????

import sys
sys.stdin = open('B.txt')

import itertools


def dfs(a, b, i):
    global check
    if visited[a][b] == 0:
        visited[a][b] = 1
        if i == N:
            return
    else:
        check += 1
        return
    if c[i] == 'E':
        dfs(a, b+1, i+1)
    elif c[i] == 'W':
        dfs(a, b-1, i+1)
    elif c[i] == 'S':
        dfs(a-1, b, i+1)
    elif c[i] == 'N':
        dfs(a+1, b, i+1)


N, *directions = map(int, input().split())

new_directions = []
direction = ['E', 'W', 'S', 'N']
for d in range(4):
    if directions[d] != 0:
        for _ in range(100 // directions[d]):
            new_directions.append(direction[d])

perm = list(itertools.permutations(new_directions, N))
perm = list(set(perm))

check = 0
for c in perm:
    visited = [[0] * (2 * N + 1) for _ in range(2 * N + 1)]
    dfs(N//2, N//2, 0)

answer = round(1 - check / len(perm), 2)
print(f'{answer}')
