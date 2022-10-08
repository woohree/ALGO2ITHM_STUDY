# 1:00
# 한 컴퓨터가 웜 바이러스에 걸리면 연결되어 있는 모든 컴퓨터는 웜 바이러스

import sys
sys.stdin = open('B.txt')

computer = int(input())  # node
N = int(input())  # edge
links = [list(map(int, input().split())) for _ in range(N)]  # graph

virus = [1]
while 1:
    # while 돌 때마다 중복값 없애서 시간 단축
    virus = list(set(virus))
    # memory에 길이 기억
    memory = len(virus)
    for link in links:
        for i in range(len(virus)):
            if link[0] == virus[i]:
                virus.append(link[1])
            elif link[1] == virus[i]:
                virus.append(link[0])
    # for문 돌고 왔는데도 virus에 추가된 데이터가 없으면 break
    if memory == len(set(virus)):
        break

# 한번 더 중복 데이터 정리
virus = set(virus)
print(len(virus) - 1)
