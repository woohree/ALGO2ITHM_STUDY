import sys
sys.stdin = open('L.txt')


N, M = map(int, sys.stdin.readline().rstrip().split())
site_dict = {}
for _ in range(N):
    temp = sys.stdin.readline().rstrip().split()
    site_dict.setdefault(temp[0], temp[1])              # 키는 url, 값은 비밀번호로 딕셔너리에 저장

for _ in range(M):
    temp2 = sys.stdin.readline().rstrip()
    print(site_dict[temp2])                             # 찾는 url을 키로 값을 찾아 출력