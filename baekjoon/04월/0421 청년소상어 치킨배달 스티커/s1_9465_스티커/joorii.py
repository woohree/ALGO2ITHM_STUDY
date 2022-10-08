import sys
sys.stdin = open('M.txt')

T = int(input())

for _ in range(T):
    N = int(input())
    scores = [[0, 0] + list(map(int, input().split())) for _ in range(2)]

    for j in range(2, N + 2):
        for i in range(2):
            scores[i][j] = max(scores[i - 1][j - 2] + scores[i][j], scores[i - 1][j - 1] + scores[i][j])

    print(max(scores[0][-1], scores[1][-1]))

