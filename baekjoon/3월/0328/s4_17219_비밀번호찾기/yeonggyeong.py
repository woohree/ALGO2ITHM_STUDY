import sys
sys.stdin = open('G.txt')

N, M = map(int, input().split())

# 주소 : 비밀번호 형태로 저장
passwords = {}

for _ in range(N):
    url, password = input().split()
    passwords[url] = password

for _ in range(M):
    want = input()
    print(passwords[want])
