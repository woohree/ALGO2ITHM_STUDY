# 가로 2칸, 세로 N칸
# 사자들은 대각선으로 배치
# 사자를 한 마리도 배치하지 않는 경우도 하나의 경우의 수
import sys
sys.stdin = open('B.txt')

N = int(input())

lion = [1, 3]

for i in range(2, N + 1):
    temp = (lion[i - 2] + lion[i - 1] * 2) % 9901
    lion.append(temp)

print(lion[-1])
