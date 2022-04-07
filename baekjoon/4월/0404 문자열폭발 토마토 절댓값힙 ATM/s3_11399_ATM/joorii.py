import sys
sys.stdin = open('M.txt')

N = int(input())
times = sorted(list(map(int, input().split())))
result = 0

for i in range(N + 1):
    for j in range(i):
        result += times[j]

print(result)
