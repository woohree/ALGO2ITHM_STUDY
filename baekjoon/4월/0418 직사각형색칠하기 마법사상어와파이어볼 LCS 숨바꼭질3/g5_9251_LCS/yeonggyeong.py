import sys
sys.stdin = open('G.txt')

string1 = list(input())
string2 = list(input())
            
dp = [[0 for _ in range(len(string1) + 1)] for _ in range(len(string2) + 1)]
answer = 0

for i in range(len(string1)):
    for j in range(len(string2)):
        if string1[i] == string2[j]:
            dp[j+1][i+1] = dp[j][i] + 1
            answer = max(answer, dp[j+1][i+1])
        else:
            dp[j+1][i+1] = max(dp[j][i+1], dp[j+1][i])

print(answer)