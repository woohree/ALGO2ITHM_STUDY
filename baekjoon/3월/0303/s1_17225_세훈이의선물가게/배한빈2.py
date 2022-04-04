import sys
sys.stdin = open('B.txt')

A, B, N = map(int, input().split())
orders = [list(input().split()) for _ in range(N)]

dp = [[] for _ in range(100)]

n = 1
sangmin = []
jisoo = []
for i in range(N):
    if orders[i][1] == 'B':
        dp[int(orders[i][0])].append(n)
        sangmin.append(n)
        n += 1
        a = A
        for j in range(1, int(orders[i][2])):
            dp[int(orders[i][0]) + a].append(n)
            sangmin.append(n)
            n += 1
            a += A
    elif orders[i][1] == 'R':
        dp[int(orders[i][0])].append(n)
        jisoo.append(n)
        n += 1
        b = B
        for j in range(1, int(orders[i][2])):
            dp[int(orders[i][0]) + b].append(n)
            jisoo.append(n)
            n += 1
            b += B

print(len(sangmin))
print(*sangmin)
print(len(jisoo))
print(*jisoo)
