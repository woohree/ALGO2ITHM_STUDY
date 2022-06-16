import sys
from itertools import combinations
sys.stdin = open('B.txt')


def dfs(r):
    global ans
    if r == 15:
        ans = 1
        for team in teams:
            if sum(team) != 0:
                ans = 0
                return
        return

    match1, match2 = matches[r]
    for x, y in ((0, 2), (1, 1), (2, 0)):  # 승 패 / 무 무 / 패 승
        if teams[match1][x] > 0 and teams[match2][y] > 0:
            teams[match1][x] -= 1
            teams[match2][y] -= 1
            dfs(r+1)
            teams[match1][x] += 1
            teams[match2][y] += 1


answer = ''
matches = list(combinations(range(0, 6), 2))  # 모든 경기 경우의 수
for _ in range(4):
    group = list(map(int, input().split()))
    teams = [group[i:i+3] for i in range(0, 18, 3)]
    ans = 0
    dfs(0)
    if ans:
        answer += '1 '
    else:
        answer += '0 '
print(answer.rstrip())
