import sys
sys.stdin = open('G.txt')

from itertools import combinations

def solution(turn):
    global comb, result
    if turn == 16:
        if sum(map(sum, teams)) == 0:
            result = 1
        return
    
    t1, t2 = comb[turn-1]
    for x, y in ([0, 2], [1, 1], [2, 0]):
        if teams[t1][x] > 0 and teams[t2][y] > 0:
            teams[t1][x] -= 1
            teams[t2][y] -= 1
            solution(turn + 1)
            teams[t1][x] += 1
            teams[t2][y] += 1


for _ in range(4):

    games = list(map(int, sys.stdin.readline().rstrip().split()))
    teams = []
    for i in range(0, len(games)-1, 3):
        teams.append(games[i:i+3])

    comb = list(combinations(range(6), 2))
    result = 0
    solution(1)
    print(result)

