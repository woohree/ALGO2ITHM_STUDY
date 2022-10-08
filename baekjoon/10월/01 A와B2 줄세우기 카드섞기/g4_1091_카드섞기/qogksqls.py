import sys
sys.stdin = open('B.txt')

'''
1. memories로 중복체크
2. 조건 실행하고 카드들이 P와 순서가 같아지면 break
'''

N = int(sys.stdin.readline().rstrip())
P = list(map(int, sys.stdin.readline().rstrip().split()))
S = list(map(int, sys.stdin.readline().rstrip().split()))

cards = [0, 1, 2] * (N//3)
result = 0
memories = [cards]
while cards != P:
    temp = cards[:]
    new = [0] * N
    for i in range(N):
        new[i] = temp[S[i]]
    cards = new
    result += 1
    if cards in memories:
        result = -1
        break

print(result)
