import sys
sys.stdin = open('input.txt')

C, N = map(int, input().split())
money_city = sorted([list(map(int, input().split())) for _ in range(N)])
count = (0+C)
while 1:
