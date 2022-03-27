# input()과 sys.stdin.readline()의 시간차...
# input() : 12864ms
# readline() : 308ms
import sys
sys.stdin = open('M.txt')

# 사이트 주소의 수 N, 비밀번호를 찾으려는 사이트 주소의 수 M
N, M = map(int, sys.stdin.readline().split())
info = {}

for _ in range(N):
    site, password = map(str, sys.stdin.readline().split())
    info[site] = password

for _ in range(M):
    print(info[sys.stdin.readline().rstrip()])
