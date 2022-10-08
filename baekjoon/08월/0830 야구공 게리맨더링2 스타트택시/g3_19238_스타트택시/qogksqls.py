import sys
sys.stdin = open('B.txt')

N, M, f = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]
now = list(map(int, input().split()))
passenger = []
goal = []
for _ in range(M):
    a, b, c, d = map(int, input().split())
    passenger.append([a, b])
    goal.append([c, d])

print(goal)
