from itertools import combinations
import sys
sys.stdin = open('M.txt')


def worldcup(idx):
    global result

    if idx == 15:       # 15 경기를 모두 끝냈을 때
        result = 1
        for team in lst:
            if sum(team) != 0:
                result = 0
                break
        return

    team_one, team_two = games[idx]     # 경기 조합
    scores = ((0, 2), (1, 1), (2, 0))
    for x, y in scores:
        if lst[team_one][x] > 0 and lst[team_two][y] > 0:       # 경기가 남아있을 때
            lst[team_one][x] -= 1
            lst[team_two][y] -= 1
            worldcup(idx + 1)
            lst[team_one][x] += 1       # 복구
            lst[team_two][y] += 1       # 복구


games = list(combinations(range(6), 2))         # 2팀씩 6경기
answer = []

for i in range(4):
    lists = list(map(int, sys.stdin.readline().split()))
    lst = [lists[j:j + 3] for j in range(0, 16, 3)]
    result = 0
    worldcup(0)
    answer.append(result)

print(*answer)
