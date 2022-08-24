import sys
sys.stdin =open('input.txt')

a,b = map(int,input().split())

field = [[0 for _ in range(a)] for _ in range(b)]
print(field)
n,m = map(int,input().split())
for i in range(n):
