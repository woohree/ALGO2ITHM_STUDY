# 25분

import sys
sys.stdin = open('B.txt')

N, M = map(int, input().split())

# 처음에는 이렇게 받았다가 시간초과 남
# urls_password = [sys.stdin.readline().rstrip().split() for _ in range(N)]

# dictionary 로 input 받음
urls_password_dict = {}
for _ in range(N):
    urls, password = sys.stdin.readline().rstrip().split()
    urls_password_dict[urls] = password

what_its_password = [sys.stdin.readline().rstrip() for _ in range(M)]

for i in range(M):
    print(urls_password_dict[what_its_password[i]])
