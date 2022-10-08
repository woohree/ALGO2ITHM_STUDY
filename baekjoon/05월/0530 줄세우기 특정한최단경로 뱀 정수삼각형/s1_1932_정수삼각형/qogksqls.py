import sys
sys.stdin = open('B.txt')

n = int(sys.stdin.readline().rstrip())
dp = [0, int(sys.stdin.readline().rstrip()), 0]  # [0, 7, 0]

for _ in range(n-1):
    numbers = list(map(int, sys.stdin.readline().rstrip().split()))
    temp = [0]
    for i in range(len(numbers)):
        temp.append(max(dp[i], dp[i+1]) + numbers[i])  # 위에 2개 중에 큰거랑 자기랑 더함
    temp.append(0)
    dp = temp[:]
print(max(dp))
